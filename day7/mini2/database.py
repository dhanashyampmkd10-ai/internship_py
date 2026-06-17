import sqlite3

DB_NAME = "app.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def get_tasks():
    conn = get_connection()

    rows = conn.execute("SELECT * FROM tasks").fetchall()

    conn.close()

    return [dict(row) for row in rows]