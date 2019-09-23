class Employee:
    def __init__(self, name, id, age, salary):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, id, age, salary, designation):
        self.designation = designation
        super(Manager, self).__init__(name, id, age, salary)
        self.list_of_employee = []

    def hire(self, cand):
        if cand.qualification.cgpa>5:
            isHired = True
            self.list_of_employee.append(cand)
        else:
            isHired = False
        return isHired

    def fire(self, emp):
        if emp in self.list_of_employee:
            isFired = True
            self.list_of_employee.remove(cand)
        else:
            isFired = False
        return isFired


class Candidate:
    def __init__(self, name, age, qualification):
        self.name = name
        self.age = age
        self.qualification = qualification


class Qualification:
    def __init__(self, degree, branch, cgpa):
        self.degree = degree
        self.branch = branch
        self.cgpa = cgpa

qual = Qualification('BE', 'Mechanical', 5.76)
cand = Candidate('sachin', 23, qual)
mgr = Manager('xyz', '#001', 40, 600000.89, "HR manager")
emp = Employee('qwe', '#002', 23, 532768.37)
if mgr.hire(cand):
    print("congrats you are hired")
else:
    print("sorry you are not hired")
