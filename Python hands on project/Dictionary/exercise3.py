
# users={
#     'rjames':{
#         'firstname':'Robin',
#         'lastname':'James',
#         'location':'Kirinyaga',
#     },
#     'robiri':{
#         'firstname':'robin',
#         'lastname':'obiri',
#         'location':'kisii',
#     },
# }
#Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person
person_1={
    'firstname':'robin',
    'lastname':'james',
    'city':'nairobi',
}
person_2={
    'firstname':'james',
    'lastname':'robin',
    'city':'kutus',
}
person_3={
    'firstname':'obiri',
    'lastname':'robins',
    'city':'kisii',
}
peoples=[person_1,person_2,person_3]

print('These is peoples information: ' + '\n')
for people in peoples:
    print('FirstName: ', people['firstname'])
    print('LastName: ', people['lastname'])
    print('City:', people['city'])
    print()

# Make several dictionaries, where the name of each dictionary is the 
# name of a pet. In each dictionary, include the kind of animal and the owner’s 
# name. Store these dictionaries in a list called pets. Next, loop through your list 
# and as you do print everything you know about each pet.

johhny={
    'name':'johhny',
    'type':'cat',
    'owner':'kamau',
}
mikey={
    'name':'mikey',
    'type':'dog',
    'owner':'jose'
}
oswald={
    'name':'oswald',
    'type':'rabbit',
    'owner':'jamal',
}

pets=[johhny,mikey,oswald]

print('The following are pets data and their owners.')
for pet in pets:
    print("Name: ", pet['name'].title())
    print("Type: ", pet['type'].title())
    print("Owner: ", pet['owner'].title())
    print()
# Make a dictionary called favorite_places. Think of three 
# names to use as keys in the dictionary, and store one to three favorite places 
# for each person. To make this exercise a bit more interesting, ask some friends 
# to name a few of their favorite places. Loop through the dictionary, and print 
# each person’s name and their favorite places.
favorite_places={
    'robin':'kisumu',
    'james':'kirinyaga',
    'obiri':'mombasa',
}

for favorite in favorite_places:
    print("Robin's favorite place is " + favorite_places['robin'].title())
    print("James's favorite place is " + favorite_places['james'].title())
    print("Obiri's favorite place is " + favorite_places['obiri'].title())
    break

# Modify your program from Exercise 6-2 (page 102) so 
# each person can have more than one favorite number. Then print each person’s 
# name along with their favorite numbers.
favorite_numbers={
    'john':3,
    'mwangi':2,
    'val':2,
    'dory':7,
    'bull':9,
    'robin':1,
}
print("The following shows people's favorite numbers:")
print('John: '+str(favorite_numbers['john']))
print('Mwangi: '+str(favorite_numbers['mwangi']))
print('Val: '+str(favorite_numbers['val']))
print('Dory: '+str(favorite_numbers['dory']))
print('Bull: '+str(favorite_numbers['bull']))
print('Robin: '+str(favorite_numbers['robin']))

# Dictionary of favorite numbers
favorite_numbers = {
    "Alice": [7, 11, 22],
    "Bob": [3, 8],
    "Charlie": [13, 17, 25]
}

# Looping through the dictionary and printing each person's name and favorite numbers
for person, numbers in favorite_numbers.items():
    print(person + "'s favorite numbers are:")
    for number in numbers:
        print("- " + str(number))
    print()  # For a newline between each person's information

# Make a dictionary called cities. Use the names of three cities as 
# keys in your dictionary. Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one fact 
# about that city. The keys for each city’s dictionary should be something like 
# country, population, and fact. Print the name of each city and all of the infor￾mation you have stored about it
cities={
    'nairobi':{
        'country':'Kenya',
        'population':'5 million',
        'fact':'industrial center',
    },
    'mombasa':{
        'country':'Kenya',
        'population':'4 million',
        'fact':'tourist attraction center'
    },
    'kigali':{
        'country':'Rwanda',
        'population':'3 million',
        'fact':'technological center'
    },
}

for city, info in cities.items():
    print(city.title() + "'s information is as follows:")
    print('- Country:',info['country'])
    print('- Population:',info['population'])
    print('- Fact:',info['fact'])
    print()

