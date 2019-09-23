class Library:
    working_hours = 24
    def __init__(self, name, location):
        self.name = name
        self.location = location

    @classmethod
    def change_time(cls, new_time):
        cls.working_hours = new_time

class Librarian:
    def __init__(self,name,gender,qualification,experience):
        self.name = name
        self.gender = gender
        self.qualification = qualification
        self.experience = experience
        self.list_of_books = []

    def find_total_books(self):
        return len(self.list_of_books)
    def open_lib(self):
        return "library opened"
    def issue_book(self,book_name):
        self.list_of_books.remove(book_name)
        return "book issued"
    def add_book(self,book_name):
        self.list_of_books.append(book_name)
        return "book added"
    def impose_fine(self):
        return "pay fine"
    def close_lib(self):
        return "library closed"

class Book:
   def __init__(self, name,author,publication, price, genre):
       self.name = name
       self.author = author
       self.publication = publication
       self.price = price
       self.genre = genre
   def show_details(self):
       return"{} {} {} {} {}".format(self.name, self.author, self.publication, self.price, self.genre)

class Member:
   def __init__(self, name, id, address):
       self.name = name
       self.id = id
       self.address = address
   def borrow_book(self):
       return "The book is borrowed"
   def return_book(self):
       return "The book is returned"
   def pay_fine(self):
       return "The fine to be paid"


sachin = Member("sachin", "#001", "bangalore")
saurabh =  Member("saurabh", "#002", "bangalore")
rsagarwal = Librarian("rsagarwal",True, "3rd grade",50)
rdsharma = Book("rdsharma","sharmaji","shawarma",100,"shorma")
rsagarwal.list_of_books.append(rdsharma)
library = Library("420","bangalore")
print("Total number of books in library",rsagarwal.find_total_books())