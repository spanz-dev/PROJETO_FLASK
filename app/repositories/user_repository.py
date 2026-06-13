import sqlite3
from config import DATABASE

def conn():
    c = sqlite3.connect(DATABASE)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    c = conn()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)
    c.commit()
    c.close()

def get_all():
    c = conn()
    r = c.execute("SELECT * FROM users").fetchall()
    c.close()
    return r

def get_by_id(id):
    c = conn()
    r = c.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
    c.close()
    return r

def create(name):
    c = conn()
    c.execute("INSERT INTO users (name) VALUES (?)", (name,))
    c.commit()
    c.close()

def update(id, name):
    c = conn()
    c.execute("UPDATE users SET name = ? WHERE id = ?", (name, id))
    c.commit()
    c.close()

def delete(id):
    c = conn()
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    c.commit()
    c.close()