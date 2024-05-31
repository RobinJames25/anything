# add several lines to the end of the program that Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
my_foods=['pizza','falafel','carrot cake','ice cream','cannoli','burger']
print("The first three items in the list are:")
print(my_foods[:3])
print("\n")
# Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
print("The three items from the middle of the list are:")
print(my_foods[3:])
print("\n")
#Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.
print("The last three items in the list are:")
print(my_foods[-3:])
print("\n")

#. Make a copy of the list of pizzas, and call it friend_pizzas.
my_pizzas=['Macaroni','Cheese','Pepperoni']
friend_pizzas=my_pizzas[:]

#Add a new pizza to the original list.
my_pizzas.append('tomato')

#Add a different pizza to the list friend_pizzas
friend_pizzas.append('onion')

# Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the sec￾ond list. Make sure each new pizza is stored in the appropriate list
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("My friend's favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza.title())