# s = 'My name is Varun and my phone number is +91 98604 00249'
# l = s.split(' ')
# p = [x for x in l if x[0]=='+' or x.isdigit()]
# for i in p:
#     print(i,end=' ')
# print('')

# s = 'My name is Varun and my phone number is varun.rathore@outlook.com'
# l = s.split(' ')
# for i in l:
#     for j in range(0,len(i)):
#         if (i[j]=='@'):
#             print(i)

import re
n = int(input())
l = []
for i in range(n):
    num = input()
    regex = re.compile(r"^([7-9]{1}[0-9]{9})$")
    matches = regex.search(num)
    if matches is not None:
        l.append("YES")
    else:
        l.append("NO")
for i in l:
    print(i)