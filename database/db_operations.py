from sqlalchemy import Table, MetaData, Column, Integer, String, inspect
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class DBOperations:
    def __init__(self, engine):
        self.engine = engine
        self.metadata = MetaData()

    def create_table(self, create_table_query: str, table_name: str):
        """
        Creates a database table if it does not already exist.

        Args:
            create_table_query (str): The SQL query to create the table.
            table_name (str): The name of the table to be checked or created.

        Returns:
            None

        Side Effects:
            - Executes the `create_table_query` to create the table if it does not exist.
            - Prints a success or information message regarding the table's creation status.
            - Logs an error message if the table creation fails.

        Raises:
            None: Any exceptions are caught and handled by logging or printing an error message.
        """
        try:
            inspector = inspect(self.engine)
            # Check if the table exists
            if not inspector.has_table(table_name):
                with self.engine.connect() as conn:
                    conn.execute(text(create_table_query))  # Execute the query
                    conn.commit()
                print(f"Table '{table_name}' created successfully.")
            else:
                print(f"Table '{table_name}' already exists.")
        except SQLAlchemyError as e:
            print(f"Error creating table '{table_name}': {e}")


    def insert_data(self, table_name, data):
        """
        Insert data into a table. If the table doesn't exist, it creates it first.
        :param table_name: Name of the target table.
        :param data: List of dictionaries with column-value pairs.
        """
        try:
            # After ensuring the table exists, insert data
            table = Table(table_name, self.metadata, autoload_with=self.engine)

            with self.engine.connect() as conn:
                conn.execute(table.insert(), data)
                conn.commit()

            logger.info(f"Inserted {len(data)} records into '{table_name}'.")
        except SQLAlchemyError as e:
            logger.error(f"Error inserting data into '{table_name}': {e}")
            raise

    def table_exists(self, table_name):
        """
        Check if a table exists in the database.
        :param table_name: Name of the table.
        :return: True if the table exists, False otherwise.
        """
        try:
            # Reflect the table to check if it exists
            Table(table_name, self.metadata, autoload_with=self.engine)
            return True
        except SQLAlchemyError:
            return False

    def query_data(self, sql_query):
	    """
	    Execute a raw SQL query and return the result as a Pandas DataFrame.
	    :param sql_query: The raw SQL query to execute.
	    :return: Pandas DataFrame containing the query result.
	    """
	    try:
	        with self.engine.connect() as conn:
	            # Use pd.read_sql to execute the query and return the result as a DataFrame
	            df = pd.read_sql(sql_query, conn)
	            logger.info(f"Executed query: {sql_query}")
	            return df
	    except SQLAlchemyError as e:
	        logger.error(f"Error executing query: {e}")
	        raise

    def delete_data(self, table_name, filters):
        """
        Delete data from a table.
        :param table_name: Name of the table to delete from.
        :param filters: SQLAlchemy filter expressions for WHERE clause.
        """
        try:
            table = Table(table_name, self.metadata, autoload_with=self.engine)
            with self.engine.connect() as conn:
                conn.execute(table.delete().where(filters))
            logger.info(f"Deleted records from '{table_name}'.")
        except SQLAlchemyError as e:
            logger.error(f"Error deleting data from '{table_name}': {e}")
            raise
