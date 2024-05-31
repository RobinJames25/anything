# # Write a program that asks the user what kind of rental car they 
# # would like. Print a message about that car, such as “Let me see if I can find you 
# # a Subaru.”

car=input("What type of car would you like? ")

print("Let me see if i can find you a " + car +' .')

# # Write a program that asks the user how many people 
# # are in their dinner group. If the answer is more than eight, print a message say￾ing they’ll have to wait for a table. Otherwise, report that their table is ready.
reservation=input("Hello, how many people are in your dinner group? ")
reservation=int(reservation)
if reservation > 8:
    print("Sorry but you'll have to wait for a table.")
else:
    print("Your table is ready!")

# Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not.
number=input("Please enter a number: ")
number=int(number)
if number%10 ==0:
    print("The number entered is a multiple of 10.")
else:
    print("The number you have entered is not a multiple of 10.")