import sqlite3
with sqlite3.connect("students.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE marks > ?",
        (70,)
    )
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Marks: {row[2]}")