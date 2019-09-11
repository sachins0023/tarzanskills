import os

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def percent(a, b):
    return (a+b)/2

def add_memory(value):
    fo = open('/home/sachin/tarzan/tarzanskills/memory.txt', 'w')
    fo.write(value)

def view_memory():
    fo = open('/home/sachin/tarzan/tarzanskills/memory.txt', 'r')
    return fo.read()

def clear_memory():
    if (os.path.exists('/home/sachin/tarzan/tarzanskills/memory.txt')):
        os.remove('memory.txt')
        print("Memory cleared")
    else:
        print("Memory doesn't exist")

index = 0

while(index>=0):
    operation = int(input("Enter the corresponding operation \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Average \n  6. View memory \n 7. Clear memory :"))
    if operation == 1:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        output = add(first_number,second_number)
        print(output)
        qn = input("Do you want to add to memory? (y/n)")
        if (qn == 'y'):
            add_memory(str(output))
    elif operation == 2:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        output = subtract(first_number,second_number)
        print(output)
        qn = input("Do you want to add to memory? (y/n)")
        if (qn == 'y'):
            add_memory(str(output))
    elif operation == 3:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        output = multiply(first_number,second_number)
        print(output)
        qn = input("Do you want to add to memory? (y/n)")
        if (qn == 'y'):
            add_memory(str(output))
    elif operation == 4:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        if (second_number == 0):
            print("Error! Division by zero not possible. Please change your values.")
            continue
        else:
            output = divide(first_number,second_number)
            print(output)
            qn = input("Do you want to add to memory? (y/n)")
            if (qn == 'y'):
                add_memory(str(output))
    elif operation == 5:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        output = percent(first_number,second_number)
        print(output)
        qn = input("Do you want to add to memory? (y/n)")
        if (qn == 'y'):
            add_memory(str(output))
    elif operation == 6:
        view_memory()
    elif operation == 7:
        clear_memory()
    else:
        print("invalid operator entered")
        continue
