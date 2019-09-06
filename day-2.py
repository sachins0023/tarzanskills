print("I will now count my chickens: ") #I will now count my chickens:
print("Hens", 25+30/6)                  #Hens 30.0
print("Roosters",100-25*3%4)            #Roosters 97
print("Now I will count the eggs: ")    #Now I will count the eggs:
print(3+2+1-5+4%2-1/4+6)                #6.75
print("Is it true that 3+2<5-7?")       #Is it true that 3+2<5-7?
print(3+2<5-7)                          #False
print("What is 3+2?",3+2)               #What is 3+2? 5
print("What is 5-7?",5-7)               #What is 5-7? -2
print("Oh, that's why it's False.")     #Oh,that's why it's False
print("How about some more.")           #How about some more.
print("Is it greater?",5>-2)            #Is it greater? True
print("Is it greater or equal?",5>=-2)  #Is it greater or equal? True
print("Is it less or equal?",5<=-2)     #Is it less or equal? False
print((25+3)*75.3)                      #2108.4
print((35/3)*(25+4.9))                  #348.833333333333333
from decimal import Decimal
print((Decimal('42.2')+Decimal('37.403'))*(Decimal('7')%Decimal('4')+Decimal('3')-Decimal('2')*Decimal('7')))       #-636.824
print(Decimal('-636.8240000000001')+Decimal('636.824'))
first_name="Sachin"
print(first_name)
first_name=23
print(first_name)
from decimal import Decimal
from fractions import Fraction
string='Happy Birthday'
int=23
float=92.8
decimal_value=99.9
fraction_value=Fraction(475,500)
decimal_value=Decimal(99.9)
bool_value= decimal_value>40
print(string,"Age",int,"Marks",float,"top",Decimal(decimal_value),"percentile","marks fraction",fraction_value,"passed",bool_value)
first_mile=1
second_mile=3
third_mile=1
first_inverse_speed=8*60+15
second_inverse_speed=7*60+12
third_inverse_speed=8*60+15
total_time= first_mile*first_inverse_speed + second_mile*second_inverse_speed + third_mile*third_inverse_speed
time_minutes=total_time/60
time_seconds=total_time%60
print(time_minutes-time_seconds/60,"mins",time_seconds,"seconds")
