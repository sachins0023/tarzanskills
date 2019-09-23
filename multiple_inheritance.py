class Father:
    def __init__(self, eye_colour):
        self.eye_colour = eye_colour

class Mother:
    def __init__(self, hair_colour):
        self.hair_colour = hair_colour

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self, "Blue")
        Mother.__init__(self, "Green")

child = Child()
print(child.eye_colour)
print(child.hair_colour)