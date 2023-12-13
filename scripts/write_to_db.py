import os, sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

import logging
import pandas as pd
from connections.postegresql_connection import PostgresConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def write_data(
        df: pd.DataFrame,
        table_name : str
        ) -> None:
        """Write DataFrame to a PostgreSQL database table.

        Parameters
        ----------
        df : pandas.DataFrame
            The DataFrame containing the data to be written.
        table_name : str
            The name of the table where the data will be written.

        Returns
        -------
        None

        Raises
        ------
        Exception
            If there is an error during the data writing process.

        Notes
        -----
        This function uses the `PostgresConnection` class to establish a connection
        to the PostgreSQL database. Ensure that the necessary environment variables
        (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME) are set before calling
        this function.
        """
        try:
            conn = PostgresConnection()

            df.to_sql(name=table_name, con=conn._instance, index=False, if_exists='replace')

            logger.info('Data written successfully')
        
        except Exception as e:
            logger.error(f"Error in the main block: {e}")

