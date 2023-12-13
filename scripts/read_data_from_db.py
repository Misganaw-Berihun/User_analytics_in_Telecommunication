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
    try:
        with PostgresConnection() as postgres_conn:
            df = pd.read_sql_query(f"SELECT * FROM {table_name};", postgres_conn)
            logger.info('Data fetched succesfully')
            return df

    except Exception as e:
        logger.error(f"Error in the main block: {e}")