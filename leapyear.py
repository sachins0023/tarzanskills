def leapyear(y):
    if(y%4==0):
        if(y%100==0):
            if(y%400==0):
                print("Year", y, "is a leap year")
            else:
                print("Year", y, "is not a leap year")
        else:
            print("Year", y, "is a leap year")
    else:
        print("Year", y, "is not a leap year")

year = int(input("Enter an year: "))
leapyear(year)