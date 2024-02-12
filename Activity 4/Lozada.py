class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

    def get_color(self):
        return self.color

    def get_model(self):
        return self.model

    def get_manufacturer(self):
        return self.manufacturer

    def __str__(self):
        return f'Car: {self.color}, {self.model}, {self.manufacturer}'

car1 = Car('blue', 'sedan', 'Toyota')
car2 = Car('red', 'hatchback', 'Honda')
car3 = Car('green', 'suv', 'Subaru')

print("Car Class:")
print(car1.get_color(), car1.get_model(), car1.get_manufacturer())
print(car2.get_color(), car2.get_model(), car2.get_manufacturer()) 
print(car3.get_color(), car3.get_model(), car3.get_manufacturer()) 

car1.color = 'black'
car1.model = 'coupe'
car2.manufacturer = 'Acura'
car3.color = 'silver'
print("")
print("After Modification:")
print(car1.get_color(), car1.get_model(), car1.get_manufacturer())
print(car2.get_color(), car2.get_model(), car2.get_manufacturer())
print(car3.get_color(), car3.get_model(), car3.get_manufacturer())
