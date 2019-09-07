print("Hello, World!")
print("Hello Again!")
print("I like typing like this.")
print("This is fun.")
print('Yay! Printing')
print("I'd much rather you 'not'")
print('I "said" do not touch this')

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

print(8/2.0)
print(8.0/2)
print(9/4)
print(9//4)
print(2++2)


name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age+height+weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

height_cm = height*2.54
weight_kg = weight*0.453592
print("Height in cm is",height_cm)
print("weight in kg is",weight_kg)

print(f"If I add %s," %age,"%f," %height, "and %r" %weight,"I get %d" %total)