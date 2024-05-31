# An ice cream stand is a specific kind of restaurant. Write 
# a class called IceCreamStand that inherits from the Restaurant class you wrote 
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of 
# the class will work; just pick the one you like better. Add an attribute called 
# flavors that stores a list of ice cream flavors. Write a method that displays 
# these flavors. Create an instance of IceCreamStand, and call this method.
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print("The restaurant's name which is " + self.restaurant_name.title())
        print("The restaurant's cuisine type which is " + self.cuisine_type.title())
        print("The restaurant has served " + str(self.number_served) + " customers.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")

    def set_number_served(self,number):
        if number >= 0:
            self.number_served=number
            print("The restaurant has served " + str(self.number_served) + " customers.")
        else:
            print("Enter a valid number.")

    def increment_number_served(self,numbers):
        self.number_served += numbers
        if numbers > 0:
            print("The following customers were served today: " + str(self.number_served))
        else:
            print("Enter a valid number...")


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type) :
         super().__init__(restaurant_name,cuisine_type)
         self.flavors = []

    def flavor_display(self):
        print("The restaurant has the following flavors: ")
        for flavor in self.flavors:
            print(flavor.title())
# Creating an instance of IceCreamStand
# ice_cream_stand=IceCreamStand('amadilo','dessert')
# # Adding some ice cream flavors
# ice_cream_stand.flavors=['vanila','chocolate','strawberry','mint chip']
# # Displaying the available ice cream flavors
# ice_cream_stand.flavor_display()


# An administrator is a special kind of user. Write a class called 
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list 
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of 
# privileges. Create an instance of Admin, and call your method

class User():
    def __init__(self,first_name,last_name,age,location):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.location= location
        self.login_attempts=0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name,age,location):
        super().__init__(first_name,last_name,age,location)
        self.privileges=Privileges()#Make a Privileges instance as an attribute in the Admin class
        # self.privileges_list=[]

    
class Privileges():
    def __init__(self) :
        self.privileges_list=[]

    def show_privileges(self):
        print("Below are a list of privileges for the admin: ")
        for privilege in self.privileges_list:
            print("-" + privilege.title())
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year) :
        """Initialize attributes to describe a car."""
        self.make=make
        self.model=model
        self.year=year
#Setting a Default Value for an Attribute
        self.odometer_reading=0

    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

    def get_descriptive_name(self) :
        """Return a neatly formatted descriptive name."""
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " +str(self.odometer_reading) + " miles on it.")
#Modifying an Attribute’s Value Through a Method
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
#Incrementing an Attribute’s Value Through a Method
    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self,make,model,year):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery=Battery()
# Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method 
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and 
# then call get_range() a second time after upgrading the battery. You should 
# see an increase in the car’s range

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=89):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " +  str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size < 70:
            print("You'll have to upgrade your battery.")
        elif self.battery_size >= 70:
            print("Battery is already upgraded.")
        # message = "This car can go approximately " + str(range)

        # message += " miles on full charge."
    def upgrade_battery(self):
        while self.battery_size <= 70:
            self.battery_size += 5
            print("upgraded battery size: " + str(self.battery_size))
        else:
            print("Battery already upgraded!")
    
# electric_car=ElectricCar('b.m.w','class s', 2017)

# print("Initial range: ")
# electric_car.battery.get_range()
# electric_car.battery.upgrade_battery()
# electric_car.battery.get_range()

    
# admin=Admin('robin','james',20,'kutus')
# admin=Admin('james','robin',20,'mwea')#Create a new instance of Admin
# admin.privileges.privileges_list=['can add post' , 'can delete post' , 'can ban user']
# # admin.privileges=['can add post' , 'can delete post' , 'can ban user']
# # admin.show_privileges()
# admin.privileges.show_privileges()