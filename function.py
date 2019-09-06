def add(a,b):
    return a+b

first_input = int(input("Enter first input number: "))
second_input = int(input("Enter second input number: "))
print("Output is : ", add(first_input,second_input))

first_input = float(input("Enter first input float: "))
second_input = float(input("Enter second input float: "))
print("Output is : ", add(first_input,second_input))

first_input = input("Enter first input number: ")
second_input = input("Enter second input number: ")
print("Output is : ", add(first_input,second_input))

from decimal import Decimal
first_input = Decimal(input("Enter first input decimal: "))
second_input = Decimal(input("Enter second input decimal: "))
print("Output is : ", add(first_input,second_input))

from fractions import Fraction
first_input = Fraction(input("Enter first input fraction: "))
second_input = Fraction(input("Enter second input fraction: "))
print("Output is : ", add(first_input,second_input))
