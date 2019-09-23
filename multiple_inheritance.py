class Father:
    def __init__(self, eye_colour):
        self.eye_colour = eye_colour

class Mother:
    def __init__(self, hair_colour):
        self.hair_colour = hair_colour

class Child(Father, Mother):
    pass

child = Child()
child.hair_colour = 'Blue'
child.eye_colour = 'pink'
