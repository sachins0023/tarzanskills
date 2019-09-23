class Living:

    def __init__(self, isBreath):
        self.isBreath = isBreath

    def breath(self):
        if self.isBreath:
            return True
        else:
            return False


class Animal(Living):

    def __init__(self, num_eyes, num_hands, num_legs, mouth):
        self.num_eyes = num_eyes
        self.num_hands = num_hands
        self.num_legs = num_legs
        self.mouth = mouth
        super(Animal,self).__init__(isBreath = True)

    def walk(self):
        if self.num_legs>=2:
            return True
        else:
            return False

    def talk(self):
        if self.mouth:
            return True
        else:
            return False


class Human(Animal):

    def __init__(self, num_eyes, num_hands, num_legs, mouth, name, mood):
        super(Human, self).__init__(num_eyes, num_hands,num_legs, mouth)
        self.name = name
        self.mood = mood

    def play(self):
        if self.mood == 'Happy':
            return True
        else:
            return False
    def eat(self):
        if self.mood == 'Hungry':
            return True
        else:
            return False

sachin = Human(2,2,2,True,'Sachin', 'Happy')
print(sachin.play())
print(sachin.eat())
print(sachin.walk())
print(sachin.talk())
print(sachin.breath())