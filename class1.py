i =0
class Faculty:
    def __init__(self):
        self.faculty_id = ""
        self.faculty_name = ""
        self.department = ""
        self.faculty_courses = ""
    def create_faculty(self):
        self.faculty_id = input("Enter faculty ID: ")
        self.faculty_name = input("Enter faculty name: ")
        self.department = input("Enter department: ")
        self.faculty_courses = ""
    def enroll_student(self, student):
        self.faculty_id = student.id
        self.faculty_name = student.name
    def display_faculty(self):
        print("ID:", self.faculty_id)
        print("Name:", self.faculty_name)
        print("Major:", self.department)
        print("Courses:", self.faculty_courses)


class Student:
    def __init__(self):
        self.student_id = ""
        self.student_name = ""
        self.major = ""
        self.student_courses = ""
        self.student_advisor = ""

    def create_new_student(self):
        self.student_id = input("Enter student ID: ")
        self.student_name = input("Enter student name: ")
        self.major = input("Enter student major: ")
        self.student_courses = ""
    def display_student(self):
        print("ID:", self.student_id)
        print("Name:", self.student_name)
        print("Major:", self.major)
        print("Courses:", self.student_courses)
        print("Advisors:", self.student_advisor)
    def assign_advisor(self):
        faculty_id = input("Enter faculty ID: ")
        for faculty in myFaculty:
            if faculty.faculty_id == faculty_id:
                self.student_advisor = faculty
                print("Student Advisor Assigned")
            else:
                print("Invalid faculty ID")

class Courses:
    def __init__(self):
        self.course_name = ""
        self.faculty = ""
    def create_course(self):
        self.course_name = input("Enter course name: ")

    def assign_faculty(self):
        faculty_id = input("Enter faculty ID: ")
        for faculty in myFaculty:
            if faculty.faculty_id == faculty_id:
                self.faculty = faculty_id
                print("Faculty assigned")
            else:
                print("Invalid faculty ID")
    def register_student(self):
        student_id = input("Enter student ID: ")
        for student in myStudents:
            if student.student_id == student_id:
                self.course_name = student.student_courses
                print("Student assigned")
            else:
                print("Invalid student ID")

myStudents = []
myFaculty = []
myCourses = []
while 1:
    print("1. Add Student")
    print("2. Add Faculty")
    print("3. Add Course")
    print("4. Display students")
    print("5. Exit")
    print("6. Assign Faculty to a course")
    print("7. Register a student to a course ")
    print("8. Display faculty")
    print("9. Assign Advisor to a student")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        new_student = Student()
        new_student.create_new_student()
        myStudents.append(new_student)
    elif choice == 2:
        new_faculty = Faculty()
        new_faculty.create_faculty()
        myFaculty.append(new_faculty)
    elif choice == 3:
        new_course = Courses()
        new_course.create_course()
        myCourses.append(new_course)
    elif choice == 4:
        for student in myStudents:
            student.display_student()
    elif choice == 5:
        exit()
    elif choice == 6:
        course_name = input("Enter course name: ")
        for course in myCourses:
            if course.course_name == course_name:
                course.assign_faculty()
    elif choice == 7:
        course_name = input("Enter course name: ")
        for course in myCourses:
            if course.course_name == course_name:
                course.register_student()
    elif choice == 8:
        for faculty in myFaculty:
            faculty.display_faculty()
    elif choice == 9:
        student_id = input("Enter student ID: ")
        for student in myStudents:
            if student.student_id == student_id:
                student.assign_advisor()
    else:
        print("Invalid choice")




