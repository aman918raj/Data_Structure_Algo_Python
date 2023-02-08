class Car:
    colour = "yellow"
    def __init__(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    @classmethod
    def set_colour2(cls, colour):
        cls.colour = colour

    @classmethod
    def get_colour2(cls):
        return cls.colour

car1 = Car("white")
print(car1.get_colour2())
car1.set_colour2("black")
print(car1.get_colour2())
car2 = Car("blue")
print(car2.get_colour2())
car2.set_colour2("orange")
print(car2.get_colour2())
print(car1.get_colour2())
