

mystack = []

def push():
    mystack.append(input("Please enter an new element: "))

def pop():
    mystack.pop()

def display():
    print(mystack)

while 1:
    print("1 add a new book to the stack")
    print("2 take a book from top of stack")
    print("3 display book stack")
    print("4 exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        push()
        print("stack has been updated")
    elif choice == "2":
        pop()
        print("stack has been updated")
    elif choice == "3":
        display()
    elif choice == "4":
        exit()
    else:
        print("Please enter a valid choice")
