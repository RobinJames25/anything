#Sorting a List Permanently with the sort() Method
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#Sorting a List Temporarily with the sorted() Function
cars=['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#Printing a List in Reverse Order
cars=['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)
cars.reverse()
print("or order")
print(cars)

#Finding the Length of a List
cars=['bmw','audi','toyota','subaru']
print(len(cars))