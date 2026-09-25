myEmployees = {}
i = 0
def add_employee():
    name = input("Please enter employee name: ")
    basepay = int(input("Please enter base pay amount: "))
    allowance = int(input("Please enter allowance amount: "))
    deductions = int(input("Please enter total deductions: "))
    taxes = int(input("Please enter total taxes: "))
    grosspay = basepay + allowance
    netpay = grosspay - deductions - taxes
    myEmployees.update(
        {"e"+str(i):{
            "name":name,
            "basepay":basepay,
            "allowance":allowance,
            "deductions":deductions,
            "taxes":taxes,
            "grosspay":grosspay,
            "netpay":netpay
        }

        }
    )
    print("Employee has been added")
i = i+1

def delete_employee():
    del myEmployees[input("Please enter e#: ")]
    print("Employee has been deleted")

def modify_employee():
    e_id = input("Please enter employee id (e#): ")
    if e_id in myEmployees:
            myEmployees[e_id]["name"] = input("Please enter new employee name: ")
            myEmployees[e_id]["basepay"] = a = int(input("Please enter new base pay amount: "))
            myEmployees[e_id]["allowance"] = b = int(input("Please enter new allowance amount: "))
            myEmployees[e_id]["deductions"] = c = int(input("Please enter new deductions: "))
            myEmployees[e_id]["taxes"] = d = int(input("Please enter new taxes: "))
            myEmployees[e_id]["grosspay"] = g = a + b
            myEmployees[e_id]["netpay"] = g - c - d
    elif e_id not in myEmployees:
        print("Please enter valid employee id (e#) ")
    else:
        print("Please enter valid employee id (e#) ")
def display_employees():
    print("Employee list: ")
    print(myEmployees)
while 1:
     print("1 Add an Employee")
     print("2 Delete an Employee")
     print("3 Modify an Employee")
     print("4 Display all Employees")
     print("5 Exit")
     choice = input("Please enter your choice: ")

     if choice == "1":
        add_employee()
     elif choice == "2":
        delete_employee()
     elif choice == "3":
        modify_employee()
     elif choice == "4":
        display_employees()
     elif choice == "5":
        exit()
     else:
        print("Please enter valid choice")

