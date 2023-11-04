import sqlite3

DATABASE_NAME = 'product_data.db'

def connect_to_db():
    """
    Connects to the SQLite database and returns the connection.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables(conn):
    """
    Creates the necessary tables in the database if they don't exist.
    """
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        machine TEXT,
        component TEXT,
        product_name TEXT,
        price_range TEXT
    )
    ''')
    
    conn.commit()

def insert_product(conn, machine, component, product_name, price_range):
    """
    Inserts a product record into the database.
    """
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO products (machine, component, product_name, price_range)
    VALUES (?, ?, ?, ?)
    ''', (machine, component, product_name, price_range))
    
    conn.commit()

# This block ensures that when the module is imported, tables are created if they don't exist.
if __name__ == "__main__":
    conn = connect_to_db()
    create_tables(conn)
    conn.close()
