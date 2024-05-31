#  Make a class called Restaurant. The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indi￾cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri￾butes individually, and then call both methods.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name.title())
        print("The restaurant's cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")

restaurant=Restaurant('amadilo','spanish')

print("The restaurant's name is " + restaurant.restaurant_name.title())
print("The cuisine type is " + restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()

# Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.
restaurant2=Restaurant('good luck', 'italian')

restaurant2.describe_restaurant()

# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods 
# for each user.
class User():
    def __init__(self,first_name,last_name,age,location):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.location= location

    def describe_user(self):
        print("\nFirstname: " + self.first_name.title())
        print("Lastname: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Location: " + self.location.title())

    def greet_user(self):
        print("\nHello to you " + self.first_name.title() + ' ' + self.last_name.title())        

user1= User('robin','obiri',20,'kutus')
user2=User('james','robin',20,'kwa governor')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

