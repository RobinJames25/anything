#Using Multiple elif Blocks
age=60

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".\n")

#Omitting the else Block
age=60

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age>=65:
    price=5

print("Your admission cost is $" + str(price) + ".")

#Testing Multiple Conditions