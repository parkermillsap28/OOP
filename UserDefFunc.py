def add():
    a = int(input("Please enter a number: "))
    b = int(input("Please enter another number: "))
    c=a+b
    print(c)
def subtract():
    a = int(input("Please enter a number: "))
    b = int(input("Please enter another number: "))
    c=a-b
    print(c)
def multiply():
    a = int(input("Please enter a number: "))
    b = int(input("Please enter another number: "))
    c=a*b
    print(c)
def divide():
    a = int(input("Please enter a number: "))
    b = int(input("Please enter another number: "))
    c=a/b
    print(c)
choice = int(input("Enter your choice: "))
if choice == 1:
    add()
elif choice == 2:
    subtract()
elif choice == 3:
    multiply()
elif choice == 4:
    divide()
