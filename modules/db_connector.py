import sqlite3
"""
This module creates a managed connection to a sqlite3 db, with exception handling (connection.rollback()) and connection handling (connection.close())

"""
# Define the context manager
class ManagedConnection:
    def __init__(self, database):
        self.database = database
        self.connection = None # TODO check this attribute

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        self.connection.isolation_level = None  # Auto-commit mode
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            # No exception occurred, commit the transaction
            self.connection.commit()
        else:
            # An exception occurred, rollback the transaction
            self.connection.rollback()
        # Close the connection
        self.connection.close()

if __name__ == "__main__":
    db_path = "enter_database_path.db"
    # Usage of the context manager
    with ManagedConnection(db_path) as db_connection:
        cursor = db_connection.cursor()
        
        try:
            # Perform your database operations
            cursor.execute("INSERT INTO your_table (column1, column2) VALUES (?, ?)", (value1, value2))
            # other operations...
            
        except sqlite3.Error as e:
            # Handle exceptions, rollback is automatically done by __exit__
            print(f"An error occurred: {e}")
        finally:
            # Ensure the cursor is closed
            cursor.close()
