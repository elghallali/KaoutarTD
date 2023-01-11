class Student:
    def __init__(self, name, roll_number, marks1, marks2):
        self.name = name
        self.roll_number = roll_number
        self.marks1 = marks1
        self.marks2 = marks2

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks in subject 1:", self.marks1)
        print("Marks in subject 2:", self.marks2)
        print("--------------------------------")

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept(self):
        name = input("Enter name: ")
        roll_number = input("Enter roll number: ")
        marks1 = int(input("Enter marks in subject 1: "))
        marks2 = int(input("Enter marks in subject 2: "))
        student = Student(name, roll_number, marks1, marks2)
        self.students.append(student)
        print("Student added to the system.")

    def display(self):
        for student in self.students:
            student.display()

    def search(self):
        roll_number = input("Enter roll number to search: ")
        for student in self.students:
            if student.roll_number == roll_number:
                student.display()
                return
        print("No student found with roll number", roll_number)

    def delete(self):
        roll_number = input("Enter roll number to delete: ")
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student with roll number", roll_number, "deleted.")
                return
        print("No student found with roll number", roll_number)

    def update(self):
        old_roll_number = input("Enter old roll number: ")
        new_roll_number = input("Enter new roll number: ")
        for student in self.students:
            if student.roll_number == old_roll_number:
                student.roll_number = new_roll_number
                print("Roll number updated.")
                return
        print("No student found with roll number", old_roll_number)

sms = StudentManagementSystem()
# Add some students to the system
numberOfStudents = int(input("Enter a number of students you can add them to the system : "))
for i in range(numberOfStudents):
    print("--------------------------------")
    sms.accept()
print("--------------------------------")

# Display all students
sms.display()

# Search for a student
sms.search()
sms.display()
print("--------------------------------")

# Update roll number of a student
sms.update()
sms.display()
print("--------------------------------")

# Delete a student
sms.delete()
sms.display()
print("--------------------------------")
