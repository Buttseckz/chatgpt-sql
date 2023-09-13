import pyodbc

class AzureSQL:
    def __init__(self, driver, server, database, user, password, encrypt):
        self.connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password};Encrypt={encrypt}"
        self.connection = None

    def connect(self):
        self.connection = pyodbc.connect(self.connection_string)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        # Convert rows to a suitable format if needed
        return rows

    def execute_schema(self, schema_query):
        cursor = self.connection.cursor()
        cursor.execute(schema_query)
        schema = cursor.fetchall()
        # Convert schema to a suitable format if needed
        return schema

    def close(self):
        if self.connection:
            self.connection.close()
