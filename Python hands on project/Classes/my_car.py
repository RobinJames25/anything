# #Importing Classes
# #Importing a Single Class
# from car import Car

# my_new_car=Car('audi','a4',2016)

# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()


# #importing an entire module

# import electric_car

# my_beetle = electric_car.Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
# my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


#Importing a module into a module
from car import Car
from electric_car import ElectricCar

my_beetle= Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())