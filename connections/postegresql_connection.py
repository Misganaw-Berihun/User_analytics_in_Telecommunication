import os, sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

import logging
from sqlalchemy import create_engine
from connections.connection_base import ConnectionBase

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PostgresConnection(ConnectionBase):
    """A class representing a connection to a PostgreSQL database.

    This class inherits from ConnectionBase, providing a standardized way to manage
    the connection to the PostgreSQL database.

    Parameters
    ----------
    **kwargs : dict
        Keyword arguments containing the database connection parameters.

    Attributes
    ----------
    _kwargs : dict
        Dictionary containing the database connection parameters.
    _raw_instance : sqlalchemy.engine.base.Engine
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _connect(self):
        """Create an instance of the underlying SQLAlchemy Engine for PostgreSQL.

        Returns
        -------
        sqlalchemy.engine.base.Engine
            The SQLAlchemy Engine instance representing the PostgreSQL database connection.

        Raises
        ------
        Exception
            If there is an error connecting to the database.
        """
        try:
            engine = create_engine(
                f"postgresql://{self._kwargs['user']}:{self._kwargs['password']}@{self._kwargs['host']}:{self._kwargs['port']}/{self._kwargs['database']}"
            )

            engine.connect()

            return engine

        except Exception as e:
            logger.error(f"Error connecting to the database: {e}")
            raise
