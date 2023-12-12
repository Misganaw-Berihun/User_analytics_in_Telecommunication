from abc import ABC, abstractmethod
from sqlalchemy.engine.base import Engine
from typing import Generic, Optional, TypeVar

RawConnectionT = TypeVar("RawConnectionT")

class ConnectionBase(ABC, Generic[RawConnectionT]):
    """The abstract base class that all connections must inherit from

        This base class provides connection authors with a way to set up 
        database parameters like database name, database password, port, and also 
        instance of database engine.
    """
    def __init__(self, **kwargs):
        """ create a BaseConnection

        Parameters
        ----------
        **kwargs: dict
            dictionary of parameters of any length to pass tho the connection class

        Returns
        -------
        None

        """
        self._kwargs = kwargs
        self._raw_instance: Optional[Engine] = self._connect()

    @property
    def _instance(self) -> RawConnectionT:
        """Get an instance of the underlying connection, creating a new one if needed."""
        if self._raw_instance is None:
            self._raw_instance = self._connect()

        return self._raw_instance

    @abstractmethod
    def _connect(self) -> RawConnectionT:
        """Create an instance of an underlying connection object.

        This abstract method is the one method that we require subclasses of
        BaseConnection to provide an implementation for. It is called when first
        creating a connection and when reconnecting after a connection is reset.

        Returns
        -------
        RawConnectionT
            The underlying connection object.
        """
        raise NotImplementedError

    def __enter__(self):
        self._raw_instance = self._connect()
        return self._raw_instance

    def __exit__(self, exc_type, exc_value, traceback):
        if self._raw_instance is not None:
            self._raw_instance.dispose()