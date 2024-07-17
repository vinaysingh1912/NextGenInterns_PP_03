class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Grade {grade} added for {self.name}.")
        else:
            print("Invalid grade. Please enter a grade between 0 and 100.")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def display_info(self):
        average_grade = self.calculate_average()
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {average_grade:.2f}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully.")
        else:
            print("A student with this ID already exists.")

    def record_grade(self, student_id, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(grade)
        else:
            print("Student ID not found.")

    def display_student_info(self, student_id):
        if student_id in self.students:
            self.students[student_id].display_info()
        else:
            print("Student ID not found.")

    def run(self):
        while True:
            print("\nStudent Grade Management System")
            print("1. Add new student")
            print("2. Record grade")
            print("3. Display student information")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                self.add_student(student_id, name)
            elif choice == '2':
                student_id = input("Enter student ID: ")
                try:
                    grade = float(input("Enter grade: "))
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the grade.")
                    continue
                self.record_grade(student_id, grade)
            elif choice == '3':
                student_id = input("Enter student ID: ")
                self.display_student_info(student_id)
            elif choice == '4':
                print("Thank You for using the service.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

# Run the Student Management System
sms = StudentManagementSystem()
sms.run()
