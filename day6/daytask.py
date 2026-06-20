import sqlite3
def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        marks INTEGER
    )
    """)
    conn.commit()
    conn.close()
def insert_student(name, marks):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )
    conn.commit()
    conn.close()
def get_all_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows
def get_student_by_id(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )
    row = cursor.fetchone()
    conn.close()
    return row
def update_marks(student_id, new_marks):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET marks = ? WHERE id = ?",
        (new_marks, student_id)
    )
    conn.commit()
    conn.close()
def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()
def get_students_above(threshold):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE marks > ?",
        (threshold,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
# ------MENU ------ #
def menu():
    create_table()
    while True:
        print("\n===== STUDENT DATABASE SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Get Student by ID")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Students Above Marks")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))
            insert_student(name, marks)
            print("Student added!")
        elif choice == "2":
            students = get_all_students()
            for s in students:
                print(s)
        elif choice == "3":
            sid = int(input("Enter ID: "))
            print(get_student_by_id(sid))
        elif choice == "4":
            sid = int(input("Enter ID: "))
            marks = int(input("Enter new marks: "))
            update_marks(sid, marks)
            print("Updated!")
        elif choice == "5":
            sid = int(input("Enter ID: "))
            delete_student(sid)
            print("Deleted!")
        elif choice == "6":
            th = int(input("Enter threshold: "))
            students = get_students_above(th)
            for s in students:
                print(s)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
menu()