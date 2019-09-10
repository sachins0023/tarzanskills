sum = 0
for index in range(1,1001):
    if (index%3 ==0 or index%5 == 0):
        sum += index
print(sum)