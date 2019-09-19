class Pokemon:
    def __init__(self,name,weight,height,type,hp,speed):
        self.name = name
        self.weight = weight
        self.height = height
        self.type = type
        self.hp = hp
        self.speed = speed

    region = "Kanto"

    @classmethod
    def change_region(cls,region):
        cls.region = region

    def attack(self):
        return self.hp*(self.weight + self.height + self.speed)

    def defend(self):
        return self.weight*(self.hp + self.height)

    def run(self):
        return self.speed*self.height - self.weight

    def print_region(self):
        return self.region

pikachu = Pokemon('Pikachu',5,3.4,'Electric',150,90)
print(pikachu.name)
print(pikachu.print_region())
raichu = Pokemon('Raichu',30,6.2,'Electric',250,60)
print(raichu.name)
print(raichu.print_region())
raichu.change_region("Hoenne")
print(raichu.print_region())
print(pikachu.print_region())