#Prints the name, salary and age inputted

first_name=input("Enter First name: ")
last_name=input("Enter Last name: ")
age=input("Enter your age: ")
salary=input("enter your salary: ")

print(type(first_name))
print(type(last_name))
print(type(age))
print(type(salary))

if type(first_name) == str and type(last_name) == str:
    print("Your name is", first_name, last_name)
else:
    print("Entered value not a name")
if type(age) == int:
    print("Your age is", age)
else:
    print("Entered value not age")
if type(salary) == float or type(salary) == int:
    print("Your salary is", salary)
else:
    print("Entered value is not salary")