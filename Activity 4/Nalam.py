class Car:
    def __init__(self, colour, model, manufacturer):
        self.colour = colour
        self.model = model
        self.manufacturer = manufacturer
        
    def display_properties(self):
        print(f"Colour: {self.colour}, Model: {self.model}, Manufacturer: {self.manufacturer}")
        
car1 = Car("Silver", "Beetle", "Volkswagen Das Auto")
car2 = Car("Red", "Ferrari La Ferrari", "Ferrari")
car3 = Car("Blue", "Raptor", "Ford")

print("\nProperties of Car 1:")
car1.display_properties()
print("\nProperties of Car 2:")
car2.display_properties()
print("\nProperties of Car 3:")
car3.display_properties()

car1.colour = "Green"
car1.model = "Convertable"

print("\nModified Properties of Car 1:")
car1.display_properties()
