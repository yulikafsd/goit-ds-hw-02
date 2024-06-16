import sqlite3
from contextlib import contextmanager

@contextmanager
def create_connection(db_file):
    """Create a database connection to SQLite database."""
    conn = sqlite3.connect(db_file)
    try:
        yield conn
        conn.commit()  # Commit if no exceptions
    except Exception as e:
        conn.rollback()  # Rollback if any exceptions
        raise e
    finally:
        conn.close()
