import logging
import pandas as pd
from postegresql_connection import PostgresConnection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


try:
    db_params = {
        'user': 'test',
        'password': 'testing_db',
        'host': 'localhost',
        'port': 5434,
        'database': 'telecom',
    }

    with PostgresConnection(**db_params) as postgres_conn:
        df = pd.read_sql_query("SELECT * FROM xdr_data;", postgres_conn)
        df.to_csv('t.csv', index=False)
        logger.info('Data written succesfully')

except Exception as e:
    logger.error(f"Error in the main block: {e}")
