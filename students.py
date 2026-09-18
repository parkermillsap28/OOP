i = 1
students = {}
while 1:
    print("1 Add a student")
    print("2 Remove a student")
    print("3 Edit a student")
    print("4 Display students")
    choice = input("Please enter your choice: ")

    if choice == "1":
        name = input("Please enter student name: ")
        major = input("Please enter major: ")
        year = input("Please enter year: ")
        students.update({"s"+str(i) : {
                            "stu_name": name,
                            "stu_major": major,
                            "stu_year": year
                                     }
                        })
        i = i + 1
        print("student has been added")
    elif choice == "2":
        del students[input("Please enter s#: ")]
        print("student has been deleted")
    elif choice == "3":
        s_id = input("Please enter s#: ")
        if s_id in students:
            students[s_id]["stu_name"] = input("Please enter new name: ")
            students[s_id]["stu_major"] = input("Please enter new major: ")
            students[s_id]["stu_year"] = input("Please enter new year: ")
        else:
            print("Student not found.")
        print("Student has been updated")
    elif choice == "4":
        print (students)
    elif choice == "5":
        exit()
    else:
        print("Please enter a valid option")