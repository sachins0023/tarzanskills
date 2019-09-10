#sum of all odd num and even num in arange inputted

start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
sum_odd = sum_even = 0
for value in range(start, end+1):
    if (value%2 == 0):
        sum_even += value
    else:
        sum_odd += value
print("Sum of even numbers between", start, "and", end, "is", sum_even)
print("Sum of odd numbers between", start, "and", end, "is", sum_odd)