from cleaning.cleaner import DataCleaner
from database.db_connector import DatabaseConnector
from database.db_operations import DBOperations
import pandas as pd

# Data Base Config
db_name = "Database Name"
db_username = "SQL Username"
db_passwd = "User Password"
db_address = "localhost"
db_url = f"postgresql+psycopg2://{db_username}:{db_passwd}@{db_address}/{db_name}"

table_name = "nasa_planetary_apod"

# Create Database Connection
db_connector = DatabaseConnector(db_url)
db_connector.connect()
db_operator = DBOperations(db_connector.engine)

# Read JSON file into a DataFrame
df = pd.read_json('data.json', lines=True)

# Create an SQL query to create a table based on the dataframe 
cleaner = DataCleaner(dataframe=df)
cleaned_data = df
create_table_query = cleaner.create_table_string(table_name)

# Create Table and Insert Data
print("Attempting to create table ", table_name)
db_operator.create_table(create_table_query, table_name)

data_dict = cleaned_data.to_dict(orient='records')
print("Attempting to insert data")
db_operator.insert_data(table_name, data_dict)
