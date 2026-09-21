

myqueue = []

def enqueue():
    myqueue.append(input("Please enter an new element: "))

def dequeue():
    myqueue.pop()

def display_queue():
    print(myqueue)

while 1:
    print("1 add a new element")
    print("2 subtract last element")
    print("3 display queue")
    print("4 exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        enqueue()
        print("queue has been updated")
    elif choice == "2":
        dequeue()
        print("queue has been updated")
    elif choice == "3":
        display_queue()
    elif choice == "4":
        exit()
    else:
        print("Please enter a valid choice")
