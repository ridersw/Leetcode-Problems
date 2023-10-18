class Vehicle:
    def __init__(self, color):
        self.color = color


class sportscar(Vehicle):
    def __init__(self, topspeed, red):
        self.color = super().__init__(red)
        self.topspeed = topspeed
        self.wheels = 4

class dumptruck(Vehicle):
    def __init__(self, isitfull):
        self.isitfull = isitfull
        self.wheel = 8


if __name__ == "__main__":
    obj = sportscar(topspeed=200, color = "red")