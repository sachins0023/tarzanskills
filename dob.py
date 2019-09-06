date_of_birth = input("Enter your birthday(dd/mm/yyyy: ")
todays_date = input("Enter today's date: ")

birth_day = int(date_of_birth[0:2])
birth_month = int(date_of_birth[3:5])
birth_year = int(date_of_birth[6:10])

todays_day = int(todays_date[0:2])
todays_month = int(todays_date[3:5])
todays_year = int(todays_date[6:10])

if birth_day>todays_day:
    day_days = (30-birth_day)+(todays_day)
    number_of_days_1 = -day_days
else:
    day_days = todays_day-birth_day
    number_of_days_1 = day_days

if birth_month>todays_month:
    month_months = (12-birth_month)+todays_month
    number_of_days_2 = 30*month_months
else:
    month_months = todays_month-birth_month
    number_of_days_2 = 30*month_months

number_of_days_3 = (todays_year-birth_year)*360
print("number of seconds i lived is", (number_of_days_1+number_of_days_2+number_of_days_3)*24*3600)