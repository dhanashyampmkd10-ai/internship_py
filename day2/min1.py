import json
students = [
    {"id": 1, "name": "shyam", "age": 20, "grade": "A"},
    {"id": 2, "name": "ayas", "age": 21, "grade": "B"},
    {"id": 3, "name": "aber", "age": 19, "grade": "A"},
    {"id": 4, "name": "sathyan", "age": 22, "grade": "C"},
    {"id": 5, "name": "appu", "age": 20, "grade": "B"}
]
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)
with open("students.json", "r") as file:
    print(file.read())
with open("students.json", "r") as file:
    students_data = json.load(file)
for student in students_data:
    print(
        f"ID: {student['id']}, "
        f"Name: {student['name']}, "
        f"Age: {student['age']}, "
        f"Grade: {student['grade']}"
    )