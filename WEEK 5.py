# ASSIGNMENT 1
# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def show_identity(self):
        print(f"I am {self.name} from {self.origin}, and my power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses their power: {self.power} ")

# Subclass: Speedster
class Speedster(Superhero):
    def __init__(self, name, origin, speed_level):
        super().__init__(name, "Super Speed", origin)
        self.speed_level = speed_level

    def use_power(self):
        print(f"{self.name} runs at speed level {self.speed_level} 🏃💨")

# Subclass: Telepath
class Telepath(Superhero):
    def __init__(self, name, origin, mind_control_level):
        super().__init__(name, "Telepathy", origin)
        self.mind_control_level = mind_control_level

    def use_power(self):
        print(f"{self.name} controls minds with level {self.mind_control_level} 🧠✨")

# Creating objects
hero1 = Speedster("FlashFire", "Metro City", 9)
hero2 = Telepath("MindMist", "Dream Realm", 8)

# Using methods
hero1.show_identity()
hero1.use_power()

hero2.show_identity()
hero2.use_power()

# ACTIVITY 2
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚢")

# Create a list of vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Use polymorphism
for vehicle in vehicles:
    vehicle.move()
