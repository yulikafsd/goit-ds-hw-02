import sqlite3
from contextlib import contextmanager

#Create a database connection to SQLite database.
@contextmanager
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    try:
        yield conn
        conn.commit()  # Commit if no exceptions
    except Exception as e:
        conn.rollback()  # Rollback if any exceptions
        raise e
    finally:
        conn.close()
