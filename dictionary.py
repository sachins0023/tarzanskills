print("Original list [11, 45, 8, 11, 23, 45, 23, 45, 89]")
l= [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict = {}
for i in l:
    count = 0
    for j in l:
        if i==j:
            count += 1
    dict[i]=count
    # for j in l:
    #     if(i==j):
    #         l.remove(i)
print(dict)
