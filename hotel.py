class Hotel:

    room_type = ['Silver', 'Gold', 'Platinum']

    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating
        self.available_rooms = range(1,10)


class Room:

    def __init__(self, room_num, room_type, price):
        if room_num in range(1,10):
            self.room_num = room_num
        else:
            print("Invalid room number")
        if room_type in hotel.room_type:
            self.room_type = room_type
        else:
            print("Enter valid room type(Silver, Gold or Platinum)")
        if self.room_num in hotel.available_rooms:
            self.availability = True
        else:
            self.availability = False
        self.price = price


class Staff:

    def __init__(self, id_num, name, age, salary):
        self.id = id_num
        self.name = name
        self.age = age
        self.salary = salary


class Manager(Staff):

    def __init__(self, id_num, name, age):
        super(Manager, self).__init__(id_num, name, age, salary = 200000)
        self.list_of_emp = []

    def hire_emp(self, emp):
        self.list_of_emp.append(emp)

    def fire_emp(self, emp):
        self.list_of_emp.remove(emp)


class Employee(Staff):

    def __init__(self, id_num, name, age, salary):
        super(Employee, self).__init__(id_num, name, age, salary)
        self.list_of_guests = []

    def add_guest(self, guest):
        self.list_of_guests.append(guest)

    def remove_guest(self, guest):
        self.list_of_guests.remove(guest)

    def bill(self, room, num_days_stay):
        return room.price*num_days_stay


class Guest:

    def __init__(self, name, id, age, gender, num_days_of_stay, visit_purpose, phone_num):
        self.name = name
        self.id = id
        self.age = age
        self.gender = gender
        self.num_days_of_stay = num_days_of_stay
        self.visit_purpose = visit_purpose
        self.phone_num = phone_num

    def book_room(self):
        print("Room booked")

    def cancel_room(self):
        print("Booking cancelled")


hotel = Hotel("Avante Garde", "Paris", 4.9)
room = Room(3, 'Platinum', 6789.67)
manager = Manager(101, "default_manager", 30)
first_employee = Employee(201, "first_employee", 25, 45676.34)
manager.hire_emp(first_employee)
second_employee = Employee(202, "second_employee", 27, 48956.56)
manager.hire_emp(second_employee)
first_guest = Guest("sachin", 1001, 24, 'M', 14, 'Business', 9876543210)
first_employee.list_of_guests.append(first_guest)
second_guest = Guest("suresh", 1002, 52, 'M', 7, 'Leisure', 8765432109)
first_employee.list_of_guests.append(second_guest)
print(help(Manager))