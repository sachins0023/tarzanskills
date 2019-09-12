n = int(input("Enter number of students: "))
dict ={}
for i in range(n):
    name = input("Enter student name: ")
    maths = float(input("Enter maths marks: "))
    physics = float(input("Enter physics marks: "))
    chemistry = float(input("Enter chemistry marks: "))
    percent = (maths+physics+chemistry)/3
    dict[name] = percent

student_name = input("Enter the name to be searched: ")
if student_name in dict:
    print("Average percentage is", round(dict[student_name],2))