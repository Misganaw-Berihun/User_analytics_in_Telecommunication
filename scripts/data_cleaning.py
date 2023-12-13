import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def drop_high_missing_columns(
    df: pd.DataFrame, 
    threshold=0.8
    ) -> pd.DataFrame:
    """Drop columns with missing values exceeding a specified threshold.

    Parameters
    ----------
    - df: DataFrame
        The dataframe of raw data set.
    - threshold: float, default 0.8
        The threshold for the percentage of missing values in a column.
        
    Returns
    -------
    - Dataframe object
        where columns specified in the columns_to_drop list, 
        which have missing values, dropped.
        
    """
    missing_percentage = df.isnull().mean()
    columns_to_drop = missing_percentage[missing_percentage > threshold].index
    df_cleaned = df.drop(columns=columns_to_drop)
    return df_cleaned

def impute_numeric_missing(
    df:pd.DataFrame, 
    columns_list:list[str],
    strategy:str='mean'
    ) -> pd.DataFrame:
    """Impute missing values for numerical columns.

    Parameters
    ----------
    - df: DataFrame
    - columns_list
        list of columnst to Impute the missing values
    - strategy: str, default 'mean'
        Imputation strategy, options: 'mean', 'zero'.

    Returns
    -------
    - Dataframe object
        with imputed missing columns from columns_list
    """
    numeric_columns = df[columns_list].select_dtypes(include='number').columns
    
    if strategy == 'zero':
        df_imputed = df.copy()  
        df_imputed[numeric_columns] = df_imputed[numeric_columns].fillna(0)
    else:
        imputation_values = df[numeric_columns].mean() if strategy == 'mean' else df[numeric_columns].median()
        df_imputed = df.copy() 
        df_imputed[numeric_columns] = df_imputed[numeric_columns].fillna(imputation_values)

    return df_imputed

def remove_rows_with_missing_values(
    df: pd.DataFrame, 
    columns_to_check: list[str]
    ):
    """
    Remove rows from a DataFrame where any of the specified columns have missing values.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    columns_to_check : list of str
        A list of column names to check for missing values. Rows will be dropped
        if any of these columns have missing values.

    Returns
    -------
    pandas.DataFrame
        A new DataFrame with rows removed where any of the specified columns have missing values.

    """
    cleaned_df = df.dropna(subset=columns_to_check, how='any')
    return cleaned_df

import pandas as pd

def replace_column_with_mode(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Replace missing values in a column with its mode.

    Parameters
    ----------
    - df: DataFrame
    - column_name: str
        Name of the column to replace missing values.

    Returns
    -------
    - DataFrame object
        with missing values in the specified column replaced by its mode.
    """

def replace_column_with_mode(
    df: pd.DataFrame, 
    column_names: list[str]
    ) -> pd.DataFrame:
    """Replace missing values in a column with its mode.

    Parameters
    ----------
    - df: DataFrame
    - column_list: list[str]
        Name of the list of columns to replace missing values.

    Returns
    -------
    - DataFrame object
        with missing values in the specified column replaced by its mode.
    """
    df_mode = df.copy()  
    for column_name in column_names:
        mode_value = df_mode[column_name].mode().iloc[0]
        df_mode[column_name] = df_mode[column_name].fillna(mode_value)

    return df_mode

def handle_outliers(
    df: pd.DataFrame, 
    columns: list[str], 
    method:str='remove'
    ) -> pd.DataFrame:
    """Handle outliers in specified columns using a specified method.

    Parameters
    ----------
    - df: DataFrame
    - columns: list
        List of columns to handle outliers.
    - method: str, default 'clip'
        Outlier handling method, options: 'clip', 'remove'

    Returns
    -------
    - Dataframe object
        where outliers are handled
    """
    if method == 'clip':
        for col in columns:
            df[col] = np.clip(df[col], df[col].quantile(0.05), df[col].quantile(0.95))
    elif method == 'remove':
        for col in columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            df = df[(df[col] >= q1 - 1.5 * iqr) & (df[col] <= q3 + 1.5 * iqr)]
    return df
