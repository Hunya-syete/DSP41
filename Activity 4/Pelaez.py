class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

# Instantiate the Car class three times
car1 = Car("black", "SUV", "Ford")
car2 = Car("Blue", "Hilux", "Toyota")
car3 = Car("Navy Green", "Civic", "Honda")

# Display properties of car1
print("Car 1:")
print("Color:", car1.color)
print("Model:", car1.model)
print("Manufacturer:", car1.manufacturer)
print()

# Display properties of car2
print("Car 2:")
print("Color:", car2.color)
print("Model:", car2.model)
print("Manufacturer:", car2.manufacturer)
print()

# Display properties of car3
print("Car 3:")
print("Color:", car3.color)
print("Model:", car3.model)
print("Manufacturer:", car3.manufacturer)
print()

# Modify properties of car1
car1.color = "Yellow"
car1.model = "Convertible"
car1.manufacturer = "Chevrolet"

# Display modified properties of car1
print("Modified Car 1:")
print("Color:", car1.color)
print("Model:", car1.model)
print("Manufacturer:", car1.manufacturer)
