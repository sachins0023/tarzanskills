import time
start_time = time.time()

def sum_of_digits(num):
    sum = 0
    string_name = str(num)
    # print(string_name)
    string_length = len(string_name)
    for i in range(string_length):
        sum += int(string_name[i:i+1])
    return sum

def factorial(num):
    factorial_num = 1
    for index in range(1, num + 1):
        factorial_num *= index
    return factorial_num

number = int(input("Enter value of n:"))
factorial_value = factorial(number)
# print(factorial_value)
sum_of_number = sum_of_digits(factorial_value)
print("The sum of", number, "! is", sum_of_number)

end_time = time.time()
print("Time required for calculation is", end_time-start_time)