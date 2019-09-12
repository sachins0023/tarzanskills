n = int(input("Enter number of students: "))
l =[]
s =[]

for i in range(n):
    name = input("Enter the name: ")
    grade = input("Enter the grade: ")
    s = [name, grade]
    l.append(s)

l.sort(key=lambda x: x[1])
print("Student having second lowest grade is:", l[1])