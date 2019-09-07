# WAP : take input for 3 students 5 marks and functions percentage, and total marks and average of class

def percent(m1,m2,m3,m4,m5):
    return (m1+m2+m3+m4+m5)/5

def total_marks(m1,m2,m3,m4,m5):
    return (m1+m2+m3+m4+m5)

def class_average(p1,p2,p3):
    return (p1+p2+p3)/3

english_1 = float(input("Enter English mark for first student: "))
english_2 = float(input("Enter English mark for second student: "))
english_3 = float(input("Enter English mark for third student: "))
hindi_1 = float(input("Enter Hindi mark for first student: "))
hindi_2 = float(input("Enter Hindi mark for second student: "))
hindi_3 = float(input("Enter Hindi mark for third student: "))
maths_1 = float(input("Enter Maths mark for first student: "))
maths_2 = float(input("Enter Maths mark for second student: "))
maths_3 = float(input("Enter Maths mark for third student: "))
physics_1 = float(input("Enter Physics mark for first student: "))
physics_2 = float(input("Enter Physics mark for second student: "))
physics_3 = float(input("Enter Physics mark for third student: "))
chemistry_1 = float(input("Enter Chemistry mark for first student: "))
chemistry_2 = float(input("Enter Chemistry mark for second student: "))
chemistry_3 = float(input("Enter Chemistry mark for third student: "))

percent1 = percent(english_1,hindi_1,maths_1,physics_1,chemistry_1)

print("Percent of marks for  student 1: ",percent1)

print("Total marks for  student 1: ",total_marks(english_1,hindi_1,maths_1,physics_1,chemistry_1))

percent2 = percent(english_2,hindi_2,maths_2,physics_2,chemistry_2)
print("Percent of marks for  student 2: ",percent2)
print("Total marks for  student 2: ",total_marks(english_2,hindi_2,maths_2,physics_2,chemistry_2))

percent3 = percent(english_3,hindi_3,maths_3,physics_3,chemistry_3)
print("Percent of marks for  student 3: ",percent3)
print("Total marks for  student 3: ",total_marks(english_3,hindi_3,maths_3,physics_3,chemistry_3))

print("Total class average:",class_average(percent1,percent2,percent3))
