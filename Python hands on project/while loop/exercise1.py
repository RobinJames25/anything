#Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value.
# As they enter each topping, 
# print a message saying you’ll add that topping to their pizza.
pizza_topppings=("Enter pizza toppings:")
pizza_topppings += ("\nEnter 'quit' when you are finished.")

while True:
    pizza=input(pizza_topppings)

    if pizza == 'quit':
        print("Your pizza is ready!")
        break
    else:
        print("We'll be adding the " + pizza + " to your pizza.\n")


