#1. Circle with constructor
import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = [math.pi * (r ** 2) for r in self.radius_list]
        return areas

    def calculate_circumference(self):
        circumferences = [2 * math.pi * r for r in self.radius_list]
        return circumferences

# Eg:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)
areas = circle.calculate_area()
circumferences = circle.calculate_circumference()

print("Areas:", areas)
print("Circumferences:", circumferences)

#2. Private variable named pi=3.141
class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list
        self.__pi = 3.141

    def calculate_area(self):
        areas = [self.__pi * (r ** 2) for r in self.radius_list]
        return areas

# Eg:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)
areas = circle.calculate_area()

print("Areas:", areas)

#3. Calculate area and perimeter
class Circle:
    __pi = 3.141
    @classmethod
    def area(cls, radius):
        return cls.__pi * (radius ** 2)
    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.__pi * radius

# Eg:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
for radius in radius_list:
    print(f"Radius: {radius}")
    print(f"Area: {Circle.area(radius)}")
    print(f"Perimeter: {Circle.perimeter(radius)}")
    print()
    
#4. UML Diagram conversion
class TV:
    def __init__(self):
        self.volume = 0
        self.channel = 0
        self.isOn = False

    def switchOn(self):
        if not self.isOn:
            self.isOn = True
            print("TV is switched ON")
        else:
            print("TV is already ON")

    def switchOff(self):
        if self.isOn:
            self.isOn = False
            print("TV is switched OFF")
        else:
            print("TV is already OFF")

    def increaseVolume(self):
        if self.isOn and self.volume < 100:
            self.volume += 4
            print("Volume increased to", self.volume)
        elif self.volume == 100:
            print("Volume is already at maximum")
        else:
            print("TV is OFF, please switch it ON")

    def decreaseVolume(self):
        if self.isOn and self.volume > 0:
            self.volume -= 2
            print("Volume decreased to", self.volume)
        elif self.volume == 0:
            print("Volume is already at minimum")
        else:
            print("TV is OFF, please switch it ON")

    def setChannel(self, channel):
        if self.isOn:
            self.channel = channel
            print("Channel set to", self.channel)
        else:
            print("TV is OFF, please switch it ON")


# Eg:
tv = TV()
tv.switchOn()
tv.increaseVolume()
tv.decreaseVolume()
tv.setChannel(43)
tv.switchOff()

#END OF TASK SESSION8 