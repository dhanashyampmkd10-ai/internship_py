import sqlite3
with sqlite3.connect("students.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE name = ?",
        ("Rahul",)
    )
    conn.commit()
    print("Student deleted successfully\n")
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Marks: {row[2]}")