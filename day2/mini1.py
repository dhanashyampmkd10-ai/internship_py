import json
students = [
    {"name": "manu", "age": 20, "mark": 85},
    {"name": "Anu", "age": 19, "mark": 90},
    {"name": "appu", "age": 21, "mark": 78},
    {"name": "athul", "age": 20, "mark": 88},
    {"name": "kanan", "age": 22, "mark": 92}
]
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)
print("Data saved to students.json")
with open("students.json", "r") as file:
    print(file.read())
with open("students.json", "r") as file:
    data = json.load(file)
print("\nStudent Details")
for student in data:
    print(f"Name: {student['name']}, Age: {student['age']}, Mark: {student['mark']}")