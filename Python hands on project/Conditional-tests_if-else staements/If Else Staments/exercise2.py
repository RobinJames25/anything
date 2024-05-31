#Tests for equality and inequality with strings
car="Audi"
print(car=="Audi")#test 1
print(car=="audi")#test 2
print(car.lower()=="audi")#test 3
print(car.upper()=="Audi")#test 4
print(car.title()=="Audi")#test 5
print(car=='bmw')#test 6

#Test whether an item is in a list
cars =['toyota' , 'bmw' ,'isuzu' ,'urus']
check='urus' in cars
print('\n')
print(check)
check='lambo' in cars
print('\n')
print(check)

#Test whether an item is not in a list
cars =['toyota' , 'bmw' ,'isuzu' ,'urus']
check="sienta"

if check not in cars:
    print(check.title()+ ", not in the cars list of items.")
else:
    print(check.title()+", is in the list of cars.")