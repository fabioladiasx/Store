import sqlite3

DATABASE = "store.db"

def get_connection():
    # I am creating a connection to my database
    connection = sqlite3.connect(DATABASE)
    # i am telling my database to behave like a normal
    # sqlite3 database.
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    connection = get_connection()

    cursor = connection.cursor()
    # orders for sql <-> Query
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_admin INTEGER DEFAULT 0

    )
    """)

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            image TEXT,
            category_id INTEGER,
            FOREIGN KEY(category_id)
                REFERENCES categories(id)
        )
    """
    )

    connection.commit()
    connection.close()


create_tables()