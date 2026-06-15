import sqlite3
with sqlite3.connect("students.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            marks INTEGER
        )
    """)
    students = [
        ("shyam", 85),
        ("Athu", 92),
        ("appu", 67),
        ("nandana", 78),
        ("devu", 95)
    ]
    for student in students:
        cursor.execute(
            "INSERT INTO students (name, marks) VALUES (?, ?)",
            student
        )
    conn.commit()
print("5 students inserted successfully")