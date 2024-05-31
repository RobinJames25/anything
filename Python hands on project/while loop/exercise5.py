# Write a program that polls users about their dream 
# vacation. Write a prompt similar to If you could visit one place in the world, 
# where would you go? Include a block of code that prints the results of the poll.

# Initialize an empty dictionary to store responses
dream_vacations={}

# Polling users about their dream vacation
while True:
    name=input("What's your name? (Enter 'quit' to exit poll): ")
    if name.lower() == 'quit':
        break
    dream_destination = input("If you could visit one place in the world, where would you go? ")

    dream_vacations[name]=dream_destination


# Printing the results of the poll
print(("\n--- Dream Vacation Poll Results ---"))

for name, desination in dream_vacations.items():
    print(name.title() + " dreams of visiting " + desination.title())