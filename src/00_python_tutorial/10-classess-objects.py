# for object oriented programming, ther's classes and objects

class Vehicle: # Class definition
    name = "" # Class variables
    kind = ""
    color = ""
    value = 0.0    

    def description(self): # a class function | self is known as the object itself
        result = f"{self.name} is a {self.color} {self.kind} worth ${self.value:.2f}"
        return result

myCar = Vehicle()
myCar.name = "My car"
myCar.kind = "car"
myCar.color = "green"
myCar.value = 50

print(myCar.description())
