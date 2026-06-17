import sqlite3

DB_NAME = "app.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def create_task(title, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, status) VALUES (?, ?)",
        (title, status)
    )

    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return task_id


def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return tasks


def get_tasks_by_status(status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE status = ?",
        (status,)
    )

    tasks = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return tasks


def get_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


def update_task(task_id, title, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title = ?, status = ?
        WHERE id = ?
        """,
        (title, status, task_id)
    )

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()