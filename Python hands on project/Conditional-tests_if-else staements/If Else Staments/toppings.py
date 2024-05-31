requested_toppings = ['mushrooms','green peppers','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")
print("\n")
#Checking for Special Items
for requested_topping in requested_toppings:
    print("Adding "+ requested_topping+ ".")
    
print("\nFinished making your pizza!")

#Checking That a List Is Not Empty
requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+ requested_topping+ ".")
        print("\nFinished making your pizza!")
    else: 
        print("\nAre you sure you want a plain pizza?") 

#Using Multiple Lists
available_toppings=['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings=['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("\nAdding " + requested_topping + ".")
    else:
        print("\nSorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

