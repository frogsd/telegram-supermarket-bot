import sqlite3

def init_db():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_order(user_id, username):
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("INSERT INTO orders (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()
  
