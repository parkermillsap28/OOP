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
        print("Book ID:", self.book_id)
        print("Book Title:", self.book_title)
        print("Author ID:", self.author_id)
        print("Publisher:", self.publisher)
        print("Year of Publication:", self.year_of_publication)
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
        print("Author ID:", self.author_id)
        print("Author name:", self.author_name)
        print("Affiliation:", self.affiliation)
        print("Country:", self.country)
        print("Phone:", self.phone)
        print("Email:", self.email)
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
        print("User ID:", self.user_id)
        print("Username:", self.user_name)
        print("Password:", self.password)
        print("Address:", self.address)
        print("Phone:", self.phone)
        print("Email:", self.email_id)
        print("Books Checked Out:", self.books_borrowed)
    def check_out_book(self):
        for book in library:
            user_id = input("Enter user id: ")
            if user.user_id == self.user_id:
                self.books_borrowed = book.book_title
                print("Book checked out")
library = []
users = []
authors = []
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
        book = Book()
        book.create_book()
        library.append(book)
        print("Book added to library")
    elif choice == "2":
        for book in library:
            book.display_books()
    elif choice == "3":
        book_id = input("Enter book id: ")
        for book in library:
            if book.book_id == book_id:
                user.check_out_book()
    elif choice == "4":
        user = User()
        user.create_user()
        users.append(user)
        print("User added")
    elif choice == "5":
        for user in users:
            user.display_user()
    elif choice == "6":
        author = Author()
        author.create_author()
        authors.append(author)
        print("Author added")
    elif choice == "7":
        for author in authors:
            author.display_author()
    elif choice == "8":
        exit()
    else:
        print("Invalid input")



