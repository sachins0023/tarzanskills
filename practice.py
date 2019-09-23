# class Staff:
#     def __init__(self, name, age, gender, dept, salary):
#         self.name = name
#         self.age = age
#         self. gender = gender
#         self.dept = dept
#         self.salary = salary
#     def teach(self):
#         return "teaches students"
#
# class Teacher(Staff):
#     def __init__(self, subject):
#         self.subject = subject
#     def exams(self):
#         return "conducts exams"
#     def punish(self):
#         return "punishes students"
#
# class Principal(Staff):
#     def __init__(self, experience):
#         self.experience = experience
#     def admit(self):
#         return "admission of student"
#     def expel(self):
#         return "expulsion of student"
#     def punish(self):
#         return "punishment of student"
#
# staff = Staff('abc', 12, True, 'qwe', 238950.98)
# teacher = Teacher('maths')
# principal = Principal(15)
# print(staff.teach(), teacher.teach(), principal.teach())
# print(help(Teacher))

# cube = lambda x: x**3# complete the lambda function
#
# def fibonacci(n):
#     f_list = []
#     if n>=0:
#         a = 0
#         f_list.append(a)
#     b = 1
#     if n>=1:
#         f_list.append(b)
#     element = a+b
#     if n>=2:
#         f_list.append(element)
#     for i in range(3,n):
#         a = b
#         b = element
#         element = element + a
#         f_list.append(element)
#     return f_list
#     # return a list of fibonacci numbers
#
# if __name__ == '__main__':
#     n = 1
#     print(list(map(cube, fibonacci(n))))

# from itertools import combinations
#
# s, k = "Hack", "2"
# s = list(s)
# k = int(k)
# l = []
# for i in range(1,k+1):
#     l.append(combinations(s,i))
#     # print(list(combinations(s,i)))
# print(l)
# for i in l:
#     print(i)

# Enter your code here. Read input from STDIN. Print output to STDOUT

# s = input()
# l = []
# i = 0
# while (i != len(s)):
#     count = 1
#     j = i + 1
#         if j == len(s):
#             break
#     while (s[j] == s[i]):
#         count += 1
#         j += 1
#         if j == len(s):
#             break
#     l.append((count, s[i]))
#     i = j
# for i in l:
#     for j in i:
#         if i.index(j) == 0:
#             print('(',j,',',end = ' ', sep =  '')
#         else:
#             print(j,')',end = ' ', sep = '')

class WordSplit:
