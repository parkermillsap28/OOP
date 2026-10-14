import pickle
class Book:
    def __init__(self):
        self.book_id = ""
        self.book_title = ""
        self.author_id = ""
        self.publisher = ""
        self.year_of_publication = ""
    def create_book(self):
        self.book_id = input("Enter book id: ")
        self.book_title = input("Enter book title: ")
        self.author_id = input("Enter author id: ")
        self.publisher = input("Enter publisher: ")
        self.year_of_publication = input("Enter year of publication: ")
    def display_books(self):
        book_file2 = open("books.dat", "rb")
        while(1):
            try:
                book = pickle.load(book_file2)
                print("Book Title:", book.book_title, "| Book ID:", book.book_id, "| Author ID:", book.author_id, "| Book Publisher:", book.publisher, "| Book Year of Publication:", book.year_of_publication)
            except EOFError:
                break
class Author:
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""
    def create_author(self):
        self.author_id = input("Enter author id: ")
        self.author_name = input("Enter author name: ")
        self.affiliation = input("Enter affiliation: ")
        self.country = input("Enter country: ")
        self.phone = input("Enter phone: ")
        self.email = input("Enter email: ")
    def display_author(self):
        author_file2 = open("author.dat", "rb")
        while (1):
            try:
                author = pickle.load(author_file2)
                print("Author Name:", author.author_name, "| Author Affiliation:", author.affiliation, "| Author country:", author.country, "| Author Phone:", author.phone, "| Author Email:", author.email)
            except EOFError:
                break
class User:
    def __init__(self):
        self.user_id = ""
        self.user_name = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email_id = ""
        self.books_borrowed = ""
    def create_user(self):
        self.user_id = input("Enter user id: ")
        self.user_name = input("Enter username: ")
        self.password = input("Enter password: ")
        self.address = input("Enter address: ")
        self.phone = input("Enter phone: ")
        self.email_id = input("Enter email: ")
    def display_user(self):
        user_file2 = open("user.dat", "rb")
        while (1):
            try:
                user = pickle.load(user_file2)
                print("User name:", user.user_name, "| User address:", user.address, "| User phone number:", user.phone, "| User email:", user.email_id)
            except EOFError:
                break
    def check_out_book(self):
        for book in b1:
            user_id = input("Enter user id: ")
            if user.user_id == self.user_id:
                self.books_borrowed = book.book_title
                print("Book checked out")
b1 = Book()
user = User()
author = Author()
while 1:
    print("1. Create Book")
    print("2. Display Books")
    print("3. Check out Book")
    print("4. Create User")
    print("5. Display User")
    print("6. Create Author")
    print("7. Display Author")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        b1.create_book()
        book_file = open("books.dat", "ab")
        pickle.dump(b1, book_file)
        book_file.close()
        print("Book added to library")
    elif choice == "2":
        b1.display_books()
    elif choice == "3":
        book_id = input("Enter book id: ")
        for book in b1:
            if b1.book_id == book_id:
                user.check_out_book()
    elif choice == "4":
        user.create_user()
        user_file = open("user.dat", "ab")
        pickle.dump(user, user_file)
        user_file.close()
        print("User added")
    elif choice == "5":
            user.display_user()
    elif choice == "6":
        author.create_author()
        author_file = open("author.dat", "ab")
        pickle.dump(author, author_file)
        author_file.close()
        print("Author added")
    elif choice == "7":
        author.display_author()
    elif choice == "8":
        exit()
    else:
        print("Invalid input")



