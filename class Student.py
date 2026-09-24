class Student:
    def __init__(self, name, GPA):
        self.name = name
        self.GPA = GPA


all_students = []

while True:
    name_input = input("Please enter the name: ")
    GPA_input = float(input("Please enter the GPA: "))

    my_student = Student(name_input, GPA_input)
    all_students.append(my_student)

    continuing = input("Do you want to continue the program? ")

    if continuing.lower() == "no":
        print("Quitting the program...")
        break


for student in all_students:
    print(f"The student name is {student.name} with {student.GPA} GPA")