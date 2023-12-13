import os, sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

import logging
import pandas as pd
from connections.postegresql_connection import PostgresConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_data(table_name='xdr_data'):
    """Read data from a PostgreSQL database table.

    Parameters
    ----------
    table_name : str, optional
        The name of the table from which to fetch data. Default is 'xdr_data'.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the data retrieved from the specified table.

    Raises
    ------
    Exception
        If there is an error during the data retrieval process.

    Notes
    -----
    This function uses the `PostgresConnection` class to establish a connection
    to the PostgreSQL database. Ensure that the necessary environment variables
    (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME) are set before calling
    this function.
    """
    try:
        with PostgresConnection() as postgres_conn:
            df = pd.read_sql_query(f"SELECT * FROM {table_name};", postgres_conn)
            logger.info('Data fetched succesfully')
            return df

    except Exception as e:
        logger.error(f"Error in the main block: {e}")