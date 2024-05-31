#Using a conditional test in the while statement:
topping = ''
while topping.lower() != 'quit':
    topping = input("Enter a topping for your pizza (enter 'quit' to finish): ")
    if topping.lower() != 'quit':
        print("Adding", topping, "to your pizza.")

#Using an active variable to control how long the loop runs:
active = True
while active:
    topping = input("Enter a topping for your pizza (enter 'quit' to finish): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print("Adding", topping, "to your pizza.")
#Using a break statement to exit the loop when the user enters a 'quit' value:
while True:
    topping = input("Enter a topping for your pizza (enter 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print("Adding", topping, "to your pizza.")

