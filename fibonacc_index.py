import time
import sys
start_time = time.time()

element = 1
index = 1
temp = 0
count = 0

while(index>=1):
    temp = element
    element += index
    count += 1
    if (10**999<=element<10**1000):
        print("The first term in the fibonacci series having 1000 digits is", count + 2)
        end_time = time.time()
        print("Time required to calculate: ", end_time - start_time)
        sys.exit()
    index = temp
