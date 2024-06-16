from sqlite3 import Error
from connect import create_connection
from create_table import read_sql_from_file, create_tables


def create_db(db_path, sql_path):
    """Create the database file and set up tables using the SQL script."""
    try:
        with create_connection(db_path) as conn:
            print(f"Database created at {db_path}")
            sql_script = read_sql_from_file(sql_path)
            create_tables(conn, sql_script)
            print("Tables created successfully.")
    except Error as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    db_path = "tasks.db"  # Path to SQLite database
    sql_path = "src/db/queries.sql"  # Path to SQL file with queries
    create_db(db_path, sql_path)
