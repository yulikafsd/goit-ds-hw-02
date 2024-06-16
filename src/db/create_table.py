import sqlite3


# Read the SQL script from file
def read_sql_from_file(filepath):
    """Reads SQL script from a file."""
    with open(filepath, "r") as file:
        sql_script = file.read()
    return sql_script


# Create tables using the SQL script
def create_tables(conn, sql_script):
    """Create tables from the SQL script.
    :param conn: Connection object
    :param sql_script: SQL script to create tables
    """
    try:
        c = conn.cursor()
        c.executescript(sql_script)
    except sqlite3.Error as e:
        print(f"An error occurred while creating tables: {e}")
        raise
