import pyodbc

# Define your connection parameters
server = 'VSL-003\SQLEXPRESS'  # e.g., 'localhost\SQLEXPRESS'
database = 'testDB'
username = 'sa'
password = 'vision'

# Create the connection string
connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + username + ';'
    'PWD=' + password
)

# Select * from BookInfo

# Establish the connection
try:
    connection = pyodbc.connect(connection_string)
    print("Connection successful!")
except Exception as e:
    print("Error: ", e)
