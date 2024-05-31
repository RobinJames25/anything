motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'#Changing the value of the first element
print(motorcycles)

motorcycles.append('kawasaki')#Adding a new element to the end of a list
print(motorcycles)

#Adding items to list dynamically
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
motorcycles.append('kawasaki')
print(motorcycles)


#inserting Elements into a list
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)
motorcycles.insert(3,'kawasaki')
print(motorcycles)

#Removing Elements from a list
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#Removing an Item Using the pop() Method
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcyle=motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a "+last_owned.title()+".")
#Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki'] 
first_owned=motorcycles.pop(0)
print('The first motorcycle I owned was a '+ first_owned.title()+'.')
print(motorcycles)

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")