def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("Error! cannot divide by zero")
    else:
        return a/b

def exponent(a,b):
    return a**b

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
operator = input("Enter one of the operators (+,-,*,/,**)")
if operator=='+':
    print("The sum is", add(first,second))
elif operator=='-':
    print("The difference is", subtract(first,second))
elif operator=='*':
    print("The product is", multiply(first,second))
elif operator=='/':
    print("The division output is", divide(first,second))
elif operator=='**':
    print("The exponential is", exponent(first,second))
else:
    print("Invalid operator")
