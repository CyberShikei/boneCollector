import pandas as pd
import logging
import re

logger = logging.getLogger(__name__)

class DataCleaner:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def clean_missing_values(self, strategy="drop", fill_value=None):
        if strategy == "drop":
            self.dataframe.dropna(inplace=True)
        elif strategy == "fill":
            self.dataframe.fillna(fill_value, inplace=True)
        else:
            logger.warning(f"Unknown missing value strategy: {strategy}")

    def normalize_columns(self, column_mapping):
        self.dataframe.rename(columns=column_mapping, inplace=True)

    def remove_duplicates(self):
        self.dataframe.drop_duplicates(inplace=True)

    def sanitize_column_names(self):
        """
        Cleans dataframe column names to prevent SQL syntax errors.
        - Replaces non-alphanumeric characters with underscores.
        - Ensures column names do not start with a digit.
        - Converts column names to lowercase for consistency.
        """
        def clean_column_name(name):
            # Replace non-alphanumeric characters with underscores
            name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
            # Ensure column name doesn't start with a number
            if name[0].isdigit():
                name = f"col_{name}"
            # Convert to lowercase
            return name.lower()

        # Apply cleaning to all columns
        cleaned_columns = {col: clean_column_name(col) for col in self.dataframe.columns}
        self.dataframe.rename(columns=cleaned_columns, inplace=True)
        logger.info(f"Sanitized column names: {cleaned_columns}")

    def _get_sql_data_types(self):
        """
        Private method to map Pandas data types to SQL data types.
        Automatically adjusts string column types based on the average length of values.
        """
        type_mapping = {
            'int64': 'BIGINT',
            'float64': 'FLOAT',
            'object': 'VARCHAR',  # Initially set to VARCHAR, but will adjust based on length
            'bool': 'BOOLEAN',
            'datetime64[ns]': 'TIMESTAMP',
            'timedelta[ns]': 'INTERVAL',
            'complex128': 'VARCHAR(255)'  # complex numbers can be stored as strings
        }
        
        sql_types = {}
        for column, dtype in self.dataframe.dtypes.items():
            dtype_str = str(dtype)
            
            if 'datetime' in dtype_str:
                sql_type = 'TIMESTAMP'  # Handle datetime types
            elif 'timedelta' in dtype_str:
                sql_type = 'INTERVAL'  # Handle timedelta types
            else:
                # For object types (i.e., strings), calculate the average length
                if dtype_str == 'object':
                    avg_length = self.dataframe[column].apply(lambda x: len(str(x)) if x is not None else 0).mean()
                    
                    # Set the length for VARCHAR based on the average length, with a buffer
                    if avg_length > 255:
                        sql_type = 'TEXT'  # Use TEXT for large strings
                    else:
                        optimal_length = int(avg_length) + 50  # Add buffer to average length
                        sql_type = f'VARCHAR({optimal_length})'
                else:
                    # Use the default mapping for non-string types
                    sql_type = type_mapping.get(dtype_str, 'VARCHAR(255)')
            
            sql_types[column] = sql_type
        
        return sql_types


    def createTblStr_sql(self, table_name: str) -> str:
        """
        Generates a SQL CREATE TABLE string based on the dataframe's schema.

        Parameters:
            table_name (str): Name of the table to be created.

        Returns:
            str: A SQL CREATE TABLE statement as a string.
        """
        # Get SQL data types using the private method
        sql_types = self._get_sql_data_types()
        
        # Start the CREATE TABLE statement
        create_statement = f"CREATE TABLE {table_name} (\n"
        
        # Add each column and its type to the statement
        columns = [f"  {col_name} {data_type}" for col_name, data_type in sql_types.items()]
        
        # Join columns with commas and newlines
        create_statement += ",\n".join(columns)
        
        # Close the table definition
        create_statement += "\n);"
        
        return create_statement

