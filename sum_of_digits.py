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

print("Sum of digits of 2^1000 is",sum_of_digits(2**1000))

end_time = time.time()
print("Time of completion is", end_time-start_time)