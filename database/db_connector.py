from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)

class DatabaseConnector:
    def __init__(self, db_url):
        """
        Initialize the DatabaseConnector with the given database URL.
        :param db_url: Database connection string (e.g., "postgresql+psycopg2://user:pass@localhost/dbname").
        """
        self.db_url = db_url
        self.engine = None
        self.Session = None

    def connect(self):
        """
        Establish a connection to the database.
        """
        try:
            self.engine = create_engine(self.db_url)
            self.Session = sessionmaker(bind=self.engine)
            logger.info("Database connection established.")
        except SQLAlchemyError as e:
            logger.error(f"Failed to connect to database: {e}")
            raise

    def get_session(self):
        """
        Get a session object for performing transactions.
        """
        if not self.Session:
            logger.error("Session is not initialized. Call `connect` first.")
            raise RuntimeError("Session is not initialized.")
        return self.Session()
