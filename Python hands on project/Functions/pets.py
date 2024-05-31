#Passing Arguments
#Positional Arguments

def describe_pet(animal_type,pet_name,animal_age=2,):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    print("My pets's age is " + str(animal_age))

describe_pet('hamster','harry')

#Multiple Function Calls
describe_pet('dog','mwangi')

#Keyword Arguments

describe_pet(animal_type='cat',pet_name='josh',animal_age='3')
describe_pet(pet_name='josh',animal_type='cat')


#Equivalent Function Calls
def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

#A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')