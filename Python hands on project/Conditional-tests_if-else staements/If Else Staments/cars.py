#Simple example
cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Checking for Inequality
requested_topping='mushrooms'
if requested_topping != 'achovies':
    print("Hold the anchovies!")

answer=17

if answer != 42:
    print("That is not the correct answer. Please try again!")

#Checking Whether a Value Is in a List
requested_topping=['mushrooms','onions','pineapple']
Answer='mushrooms' in requested_topping
print(Answer)
Answer2='pepperoni' in requested_topping
print(Answer2)

#Checking Whether a Value Is Not in a List
banned_users=['andrew','carolina','davidd']
user='marie'

if user not in banned_users:
    print(user.title() +", you can post a response if you wish.")