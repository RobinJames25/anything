# Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an 
# instance called restaurant from this class. Print the number of customers the 
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number 
# of customers that have been served. Call this method with a new number and 
# print the value again.
# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served. Call this method with any num￾ber you like that could represent how many customers were served in, say, a 
# day of business.


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

restaurant=Restaurant('amadilo', 'italian' )

# restaurant.describe_restaurant()

# restaurant.number_served=23

# restaurant.describe_restaurant()

restaurant.set_number_served(24)

restaurant.increment_number_served(14)

restaurant.increment_number_served(10)

# Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write 
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented 
# properly, and then call reset_login_attempts(). Print login_attempts again to 
# make sure it was reset to 0.
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

user=User('robin','obiri',20,'kutus')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.reset_login_attempts()

print("Login Attempts: " ,user.login_attempts)