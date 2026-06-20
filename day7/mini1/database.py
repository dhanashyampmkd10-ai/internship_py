import sqlite3

DATABASE_NAME = "app.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def create_task(task):
    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO tasks (title, completed)
        VALUES (?, ?)
        """,
        (task.title, task.completed)
    )

    conn.commit()

    task_id = cursor.lastrowid

    conn.close()

    return {
        "id": task_id,
        "title": task.title,
        "completed": task.completed
    }