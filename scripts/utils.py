import pandas as pd
from pandasql import sqldf

def get_total_download_for_each_app(
    df: pd.DataFrame, 
    attribute_1: str, 
    attribute_2: str) -> pd.DataFrame:
    """
    Perform aggregation on DataFrame based on specified attributes.

    Parameters
    ----------
    - attribute_1 (str): The column representing the first attribute for aggregation.
    - attribute_2 (str): The column representing the second attribute for aggregation.

    Returns
    -------
    pd.DataFrame: A DataFrame containing aggregated results with columns:
        - 'User_MSISDN': MSISDN/Number of the user.
        - 'Total_Download': Total download data for the user.
        - 'Total_Upload': Total upload data for the user.
        - 'Total': Total data (sum of download and upload) for the user.
    
    """
    query = f'''
        SELECT "MSISDN/Number" AS User_MSISDN,
            SUM("{attribute_1}") AS Total_Download,
            SUM("{attribute_2}") AS Total_Upload,
            (SUM("{attribute_1}") + SUM("{attribute_2}")) AS Total 
        FROM df
        GROUP BY "MSISDN/Number"
        ORDER BY Total DESC;
    '''
    return sqldf(query, locals())
