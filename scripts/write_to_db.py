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
        try:
            conn = PostgresConnection()

            df.to_sql(name=table_name, con=conn._instance, index=False, if_exists='replace')

            logger.info('Data written successfully')
        
        except Exception as e:
            logger.error(f"Error in the main block: {e}")

