import sqlite3
from contextlib import contextmanager

class LocalDatabase():

    def __init__(self, file_name = 'local_database.db'):
        
        self.file_name = file_name
        self.initialize_database()

    @contextmanager
    def connect(self):
        connection = sqlite3.connect(self.file_name)

        try:
            yield connection
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()
    
    def initialize_database(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS clients(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        telefone TEXT NOT NULL           
                )
            ''')

        print("Database successfully initialized")
