class TarzanSkills:

    def __init__(self, name, location, established_year, revenue):
        self.name = name
        self.location = location
        self.established_year = established_year
        self.revenue = revenue


class Founder:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_of_emp = []
        self.list_of_stud = []
    def pay_salary(self):
        print("Paid the salary")

    def hire_emp(self, emp):
        self.list_of_emp.append(emp)

    def fire_emp(self, emp):
        self.list_of_emp.remove(emp)

    def hire_stud(self, stud):
        self.list_of_stud(stud)

    def dismiss_stud.append.(stud):
        self.list_of_stud.remove(stud)