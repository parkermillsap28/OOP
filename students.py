i = 1
students = {}
while 1:
    print("1 Add a student")
    print("2 Remove a student")
    print("3 Replace courses")
    print("4 Display course list")
    print("5 Exit")
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
    elif choice == "3":
        students[input("Please enter s#: ")] = (
            while 1:
                input("what info would you like to change?"
                      "1 Name"
                      "2 Major"
                      "3 Year")
                choice = input("Please enter your choice: ")
                if choice == "1":
                    name = input("Please enter student name: ")
                elif choice == "2":
                    major = input("Please enter major: ")
                elif choice == "3":
                    year = input("Please enter year: ")
                else:
                    print("Please enter a valid choice"))

    print("Student has been updated")