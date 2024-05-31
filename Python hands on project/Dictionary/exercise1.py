# Print each piece of information stored in your dictionary.
person={"firstname":"robin","lastname":"okioma","age":20,"city":"kutus"}
print(person["firstname"].title()+ " " +person["lastname"].title())
print(person["age"])
print(person["city"].title())
#  Print each person’s name and their favorite number
favorite_numbers={
    'john':3,
    'mwangi':2,
    'val':2,
    'dory':7,
    'bull':9,
    'robin':1,
}

print("John's favorite number is " + str(favorite_numbers['john']))
print("Mwangi's favorite number is " + str(favorite_numbers['mwangi']))
print("Val's favorite number is " + str(favorite_numbers['val']))
print("Dory's favorite number is " + str(favorite_numbers['dory']))
print("Bull's favorite number is " + str(favorite_numbers['bull']))
print("Robin's favorite number is " + str(favorite_numbers['robin']))

#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
glossary={'dictionary':'A collection of key-pair values',
          'tuples':'An immutable list',
          'list':'A collection of items in a particular order',
          'concatenation':'Method of combining strings',
          'string':'A series of characters'
          }
print("\nDictionary")
print(glossary['dictionary'])

print("\nTuples")
print(glossary['tuples'])

print("\nList")
print(glossary['list'])

print("\nConcatenation")
print(glossary['concatenation'])

print("\nString")
print(glossary['string'])