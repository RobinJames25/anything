# Make a list called sandwich_orders and fill it with the names of vari￾ous sandwiches. Then make an empty list called finished_sandwiches. Loop 
# through the list of sandwich orders and print a message for each order, such 
# as I made your tuna sandwich. As each sandwich is made, move it to the list 
# of finished sandwiches. After all the sandwiches have been made, print a 
# message listing each sandwich that was made.
sandwich_orders=['chicken','pastrami','grilled','pastrami','pastrami','egg','ham']
finished_sandwiches=[]

# Using the list sandwich_orders from Exercise 7-8, make sure 
# the sandwich 'pastrami' appears in the list at least three times. Add code 
# near the beginning of your program to print a message saying the deli has 
# run out of pastrami, and then use a while loop to remove all occurrences of 
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 
# in finished_sandwiches.
print("Our restaurant has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_order=sandwich_orders.pop()
    print("I made you a " + sandwich_order +" sandwich.")
    finished_sandwiches.append(sandwich_order)

print("\nThe following is a list of your finished sandwich order:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
