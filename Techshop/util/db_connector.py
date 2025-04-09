import pyodbc

class DatabaseConnector:
    def __init__(self, server, database):
        # Updated connection string for Windows Authentication
        self.connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        self.connection = None

    def open_connection(self):
        try:
            self.connection = pyodbc.connect(self.connection_string)
            print("Database connection opened.")
        except Exception as e:
            print(f"Error opening connection: {e}")

    def commit(self):
        if self.connection:
            self.connection.commit()  # Commit the transaction
            print("Transaction committed.")
        else:
            print("No connection to commit.")
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def fetch_query(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
