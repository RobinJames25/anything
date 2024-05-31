#a loop that runs through the dictionary’s keys and values
glossary={'dictionary':'A collection of key-pair values',
          'tuples':'An immutable list',
          'list':'A collection of items in a particular order',
          'concatenation':'Method of combining strings',
          'string':'A series of characters'
          }


#add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output
glossary['nesting']='storing a set of dictionaries in a list'


for key in glossary.keys():
    print(key.title()+ ' -' + glossary[key].title())

#Make a dictionary containing three major rivers and the country each river runs through
Rivers={'Nile':'Egypt','Tana':'Kenya','Zambezi':'Zambia'}

#Use a loop to print a sentence about each river, such as The Nile runs through Egypt
for River in Rivers:
    print("River " + River.title() + " runs in " + Rivers[River].title())

#Use a loop to print the name of each river included in the dictionary
for River in Rivers:
    print(River.title())

#Use a loop to print the name of each country included in the dictionary
for River in Rivers:
    print(Rivers[River].title())


#Make a list of people who should take the favorite languages poll.
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

# Include some names that are already in the dictionary and some that are not
friends=['phil','sarah','edward','billy','frank',]

for name in favorite_languages:
    print(name.title() + " thank you for letting us know your favorite language which is " +favorite_languages[name].title())

    if name in friends:
        print('Hi ' + name.title() + " thank you for taking our poll.")
    
    if  'billy' not in favorite_languages:
        print("Hi  Billy kindly consider taking our poll.")
    if 'frank' not in favorite_languages:
        print("Hi Frank kindly consider taking our poll.")