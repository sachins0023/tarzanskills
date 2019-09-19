class Library:
    def __init__(self,type,location,year,librarian,num_books):
        self.type = type
        self.location = location
        self.establish_year = year
        self.librarian = librarian
        self.num_books = num_books
    def get_address(self):
        print("Address of library is printed")

class Librarian:
    def __init__(self, name,gender,age,qualification)
        self.name = name
        self.gender = gender
        self.age = age
        self.qualification = qualification
    def lend_book(self):
        print("library lend book")
    def accept_book(self):
        print("library accepts return book")
    def add_book(self):
        print("library adds new book")
    def remove_book(self):
        print("library removes book")
    def check_validity(self):
        print("librarian checks member validity")
    def check_book(self):
        print("librarian checks if book available")
    def give_fine(self):
        print("librarian gives fine if late submission or book lost")

class Book:
    def __init__(self, name,author,genre,publication):
        self.name = name
        self.author = author
        self.genre = genre
        self.publication = publication


class Member:
    def __init__(self,id,name,age,gender,occupation,interested_book):
        self.id =id
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.interest = interested_book
    def open(self):
        print("opens the book")
    def close(self):
        print("closes the book")
    def borrow_book(self):
        print("Member borrows book")
    def return_book(self):
        print("Member returns book")
    def pay_fine(self):
        print("Member pays fine")
