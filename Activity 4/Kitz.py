class Car:
    # Declare class attributes
    color = None
    model = None
    manufacturer = None

    # Define a method to display the car properties
    def display_properties(self):
        print(f'Car details:\nColor: {self.color}\nModel: {self.model}\nManufacturer: {self.manufacturer}')

# Instantiate the Car class 3 times
my_car_1 = Car()
my_car_2 = Car()
my_car_3 = Car()

# Set the properties for each car instance
my_car_1.color = "White"
my_car_1.model = "Alto800"
my_car_1.manufacturer = "Maruti"

my_car_2.color = "Green"
my_car_2.model = "I10NIOS"
my_car_2.manufacturer = "Hyundai"

my_car_3.color = "Brown"
my_car_3.model = "A8"
my_car_3.manufacturer = "Audi"

# Display the properties for each car instance
my_car_1.display_properties()
my_car_2.display_properties()
my_car_3.display_properties()

# Modify the properties of the first car instance
my_car_1.color = "Orange"
my_car_1.model = "Civic"
my_car_1.manufacturer = "Honda"

# Display the modified properties for the first car instance
print(f'Modified car details:\nColor: {my_car_1.color}\nModel: {my_car_1.model}\nManufacturer: {my_car_1.manufacturer}')
