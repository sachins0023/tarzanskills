import sys
element = 1
sum_even = 0
index = 1
temp = 0
while(index>=1):
    temp = element
    element += index
    if (element>4000000):
        print("Sum of even valued terms in Fibonacci sequence is", sum_even)
        sys.exit()
    if (element%2 == 0):
        print(element)
        sum_even += element
    index = temp