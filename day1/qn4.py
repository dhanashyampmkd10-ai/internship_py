class student:
    def __init__(self,student_id,student_name,mark):
        self.student_id=student_id
        self.student_name=student_name
        self.mark=mark
    def grade(self):
        if self.mark>=90:
            return "Grade A"
        elif self.mark>=80:
            return "Grade B"
        elif self.mark>=70:
            return "Grade C"
        elif self.mark>=60:
            return "Grade D"
        else:
            return "Grade F"
    def display(self):
        print("Student ID:",self.student_id)
        print("Student Name:",self.student_name)
        print("Mark:",self.mark)
        print("Grade:",self.grade())
print("Enter number of students:")
n=int(input())
students=[]
for i in range(n):
    print(f"\nEnter details of Student {i}")
    
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    s = student(student_id, student_name, marks)
    students.append(s)


for s in students:
    s.display()
    
