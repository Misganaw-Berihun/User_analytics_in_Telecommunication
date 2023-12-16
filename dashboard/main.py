import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import sys
import os

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

import scripts.read_data_from_db as rd

class TelecomDashboard:
    def __init__(self):
        self.eng_df = None
        self.exp_df = None
        self.satisfaction_score = None
        self.data = None

        st.set_option('deprecation.showPyplotGlobalUse', False)
    
        self.read_dataframes()

    def read_dataframes(self):
        self.eng_df = self.read_data('user_engagement')
        self.exp_df = self.read_data('user_experience')
        self.satisfaction_score = self.read_data('satisfaction_score')

    def read_data(self, table_name):
        return rd.read_data(table_name)

    def draw_histogram(self, df, column_name):
        fig, ax = plt.subplots()
        df[column_name].hist(bins=30, color="skyblue", edgecolor="black")
        ax.set_xlabel(column_name)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    def draw_3d_scatter_plot(self, df, x_column, y_column, z_column, cluster_colors):
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')


        for cluster_label, color in cluster_colors.items():
            cluster_data = df[df['Cluster'] == cluster_label]
            ax.scatter(
                cluster_data[x_column], 
                cluster_data[y_column], 
                cluster_data[z_column], 
                label=f'Cluster {cluster_label}',
                color=color
                )

        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_zlabel(z_column)

        plt.show()
        st.pyplot(fig)

    def draw_pie_chart(self, df, column_name, bins, labels):
        df['SatisfactionGroup'] = pd.cut(df[column_name], bins=bins, labels=labels, include_lowest=True)

        fig, ax = plt.subplots()
        group_counts = df['SatisfactionGroup'].value_counts()

        ax.pie(group_counts, labels=group_counts.index, autopct='%1.1f%%', startangle=90)

        st.pyplot(fig)

    def run(self):
        st.title("Telecom Data Analysis Dashboard")

        st.header("User Experience Metrics")
        col1, col2 = st.columns(2)

        with col1:
            st.write("### Average TCP")
            self.draw_histogram(self.exp_df, "AvgTCP")

        with col2:
            st.write("### Average RTT")
            self.draw_histogram(self.exp_df, "AvgRTT")

        col3, col4 = st.columns(2)

        with col3:
            st.write("### Average Throughput")
            self.draw_histogram(self.exp_df, "AvgThroughput")

        with col4:
            st.write("### clustering (k = 3)")
            cluster_colors = {0: 'red', 1: 'blue', 2:'green'}
            fig4 = self.draw_3d_scatter_plot(self.exp_df, "AvgTCP", "AvgRTT", "AvgThroughput", cluster_colors)


        st.header("User Engagement Metrics")
        col1, col2 = st.columns(2)

        with col1:
            st.write("### Session Duration")
            self.draw_histogram(self.eng_df, "SessionDuration")

        with col2:
            st.write("### Session Frequency")
            self.draw_histogram(self.eng_df, "SessionFrequency")

        col3, col4 = st.columns(2)

        with col3:
            st.write("### Total Traffic")
            self.draw_histogram(self.eng_df, "TotalTraffic")

        with col4:
            st.write("### clustering (k = 7)")
            cluster_colors = {0: 'red', 1: 'blue', 2:'green', 3:'black', 4:'yellow', 5:'brown', 6:'purple'}
            fig4 = self.draw_3d_scatter_plot(self.eng_df, "SessionDuration", "SessionFrequency", "TotalTraffic", cluster_colors)
        
        st.header("Satisfaction Score Distribution")
        bins = np.arange(0, 1.4142, 0.35355)
        labels = ["Low Satisfaction", "Medium Satisfaction", "High Satisfaction"]
        self.draw_pie_chart(self.satisfaction_score, "SatisfactionScore", bins,labels)

if __name__ == "__main__":
    dashboard = TelecomDashboard()
    dashboard.run()