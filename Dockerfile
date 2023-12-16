# Use an official Python runtime as a parent image
FROM python:3.8-slim
WORKDIR /app

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/Misganaw-Berihun/User_analytics_in_Telecommunication.git .

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Define environment variable
ENV NAME World