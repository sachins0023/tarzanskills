# l = [ 0, 1, 2, 3, 2, 1, 0 ]
# if (l[0] == l[-1]):
#     print("the first and last number of a list is same"
#           "\nresult is True")
# else:
#     print("result is false")


# l = ['qwe', 'efqrde', 'qwrqr', 'a', 'b', 'qwefqfaq', 'c', 'qrfas', 'qwe', 121]
# count = 0
# for i in l:
#     if len(str(i)) >=2:
#         if (str(i)[0] == str(i)[-1]):
#             count += 1
# print("Number of words with first and last character same is", count)

l1 = [1, 34, 45, 23, 23, 45, 55, 46, 36]
l2 = [12, 2, 23, 14, 11, 99, 90, 78, 87]
l3 = []
for i in l1:
    if i%2==1:
        l3.append(i)
for j in l2:
    if j%2==0:
        l3.append(j)
print(l3)