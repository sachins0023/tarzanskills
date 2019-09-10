import sys

value = 2
# count = 0
sum = 0

while (value):

    if value == 2:
        # count = count + 1
        sum += value

    elif value == 3:
        # count= count + 1
        sum += value
    else:
        for index in range(2,(value//2)+1):
            passcode = True
            if (value%index) == 0:
                passcode = False
                break
        if passcode:
            # count += 1
            sum += value
            print(value)

    value += 1
    if (value>=20000):
        print("Sum of all primes below 2 mill is", sum)
        sys.exit()