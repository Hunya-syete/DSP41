class Car:
    color = ""
    model = ""
    manufacturer = ""

    def set_properties(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

car1 = Car()
car1.set_properties("red", "Mazda3", "Mazda")

car2 = Car()
car2.set_properties("black", "Mustang", "Ford")

car3 = Car()
car3.set_properties("white", "Hilux", "Toyota")

print(car1.color, car1.model, car1.manufacturer)
print(car2.color, car2.model, car2.manufacturer)
print(car3.color, car3.model, car3.manufacturer)

car1.color = "Red"
car2.model = "Raptor"
car3.manufacturer = "Ford"

print(car1.color, car1.model, car1.manufacturer)
print(car2.color, car2.model, car2.manufacturer)
print(car3.color, car3.model, car3.manufacturer)
