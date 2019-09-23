class Customer:
    def __init__(self, id, name, ticket):
        self.id = id
        self.name = name
        self.ticket = ticket

class Ticket:
    def __init__(self,time, movie, seat, price):
        self.time = time
        self.movie = movie
        self.seat = seat
        self.price = price

class Seat:
    def __init__(self, seat_num, screen):
        self.seat_num = seat_num
        self.screen = screen

class Screen:
    def __init__(self, location, screen_name, movie):
        self.screen_name = screen_name
        self.location = location
        self.movie = movie

class Movie:
    def __init__(self, name, language):
        self.name = name
        self.language = language

avenger = Movie('avengers', 'english')
pvr = Screen('bengaluru', 'screen-A', avenger)
a1 = Seat('A1', pvr)
ticket_1 = Ticket('7.30 pm', avenger, a1, 200)
customer_1 = Customer('#001',"sachin",ticket_1)