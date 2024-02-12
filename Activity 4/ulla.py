class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

# Instantiate the Car class three times
car1 = Car("blue", "Sedan", "Skyline supra")
car2 = Car("white", "SUV", "Honda civic")
car3 = Car("Black", "Convertible", "ford")

# Display properties of each car
print("Car 1: Color={}, Model={}, Manufacturer={}".format(car1.color, car1.model, car1.manufacturer))
print("Car 2: Color={}, Model={}, Manufacturer={}".format(car2.color, car2.model, car2.manufacturer))
print("Car 3: Color={}, Model={}, Manufacturer={}".format(car3.color, car3.model, car3.manufacturer))

# Modify properties of Car 1
car1.color = "blue"
car1.model = "Hatchback"

# Display modified properties of Car 1
print("\nAfter modification:")
print("Car 1: Color={}, Model={}, Manufacturer={}".format(car1.color, car1.model, car1.manufacturer))
