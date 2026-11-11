import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Lab5DB"
)
cursor = db.cursor()
cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Student (
                    StudentID INT PRIMARY KEY,
                    Name VARCHAR(50),
                    Major VARCHAR(50),
                    Courses VARCHAR(50),
                    GPA VARCHAR(50)
                    )
                """)
cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Faculty (
                    FacultyID INT PRIMARY KEY,
                    Name VARCHAR(50),
                    Department VARCHAR(50),
                    Taught_Courses VARCHAR(50) 
                    )
                """)
class Student_Master:
    def __init__(self):
        self.stu_id = ""
        self.stu_name = ""
        self.stu_major = ""
        self.stu_courses = ""
        self.stu_cgpa = ""
    def add_student(self):
        self.stu_id = input("Enter Student ID: ")
        self.stu_name = input("Enter Student Name: ")
        self.stu_major = input("Enter Student Major: ")
        self.stu_courses = input("Enter Student Courses: ")
        self.stu_cgpa = input("Enter Student GPA: ")
        sql = "INSERT INTO Student VALUES (%s,%s,%s,%s,%s)"
        values = (self.stu_id, self.stu_name, self.stu_major, self.stu_courses, self.stu_cgpa)
        cursor.execute(sql, values)
        db.commit()
        print("Student created")
        return
    def display_students(self):
        cursor.execute("SELECT * FROM Student")
        for row in cursor.fetchall():
            print(row)
    def update_student(self):
        sid = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        major = input("Enter Student Major: ")
        sql = """
            UPDATE Student
            SET Name=%s,Major=%s
            WHERE StudentID=%s
            """
        cursor.execute(sql, (name, major, sid,))
        db.commit()
        print("Student updated")
    def delete_student(self):
        sid = int(input("Enter Student ID: "))
        sql = "DELETE FROM Student WHERE StudentID=%s"
        cursor.execute(sql, (sid,))
        db.commit()
        print("Student deleted")


class Faculty_Master:
    def __init__(self):
        self.fac_id = ""
        self.fac_name = ""
        self.fac_department = ""
        self.fac_teaches_courses = ""
    def add_faculty(self):
        self.fac_id = input("Enter Faculty ID: ")
        self.fac_name = input("Enter Faculty Name: ")
        self.fac_department = input("Enter Faculty Department: ")
        self.fac_teaches_courses = input("Enter taught Courses: ")
        sql = "INSERT INTO Faculty VALUES (%s,%s,%s,%s)"
        values = (self.fac_id, self.fac_name, self.fac_department, self.fac_teaches_courses,)
        cursor.execute(sql, values)
        db.commit()
        print("Faculty created")
        return
    def display_faculty(self):
        cursor.execute("SELECT * FROM Faculty")
        for row in cursor.fetchall():
            print(row)
    def update_faculty(self):
        fid = int(input("Enter Faculty ID: "))
        name = input("Enter Faculty Name: ")
        dpmt = input("Enter Faculty Department: ")
        sql = """
            UPDATE Faculty
            SET Name=%s,Department=%s
            WHERE FacultyID=%s
            """
        cursor.execute(sql, (name, dpmt, fid,))
        db.commit()
        print("Faculty updated")
    def delete_faculty(self):
        fid = int(input("Enter Faculty ID: "))
        sql = "DELETE FROM Faculty WHERE FacultyID=%s"
        cursor.execute(sql, (fid,))
        db.commit()
        print("Faculty deleted")

while True:
    print("1. Create Student")
    print("2. Create Faculty")
    print("3. Display Students")
    print("4. Display Faculty")
    print("5. Edit Students")
    print("6. Edit Faculty")
    print("7. Delete Students")
    print("8. Delete Faculty")
    print("9. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
            Student_Master().add_student()
    elif choice == "2":
            Faculty_Master().add_faculty()
    elif choice == "3":
            Student_Master().display_students()
    elif choice == "4":
            Faculty_Master().display_faculty()
    elif choice == "5":
            Student_Master().update_student()
    elif choice == "6":
            Faculty_Master().update_faculty()
    elif choice == "7":
            Student_Master().delete_student()
    elif choice == "8":
            Faculty_Master().delete_faculty()
    elif choice == "9":
        cursor.close()
        db.close()
        print("Database Closed")
        exit()
    else:
            print("Invalid Choice")
