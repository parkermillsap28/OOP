import pickle
#file1 = open("mytext.txt", "a")
#file1.writelines(input("Enter your name:"))
#file1.writelines("! This is Monday. ")
#file1.writelines("How are you? ")
#file1.close()

#file2 = open("mytext.txt", "r")
#for line in file2:
    #print(line)
#file2.close()

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
b1 = Book()
b1.create_book()
b1.display_books()

file1 = open("books.dat", "ab")
pickle.dump(b1, file1)
file1.close()

file2 = open("books.dat", "rb")
while(1):
    try:
        data = pickle.load(file2)
        print("Book ID:", data.book_id)
        print("Book Title:", data.book_title)
        print("Author ID:", data.author_id)
        print("---" * 20)
    except(EOFError):
        break