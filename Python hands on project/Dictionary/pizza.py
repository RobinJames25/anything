#Store information about pizza being ordered
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}

#Summarize your order
print('You ordered a ' +pizza['crust'] + '-crust pizza' + " with the following toppings:")

for topping in pizza['toppings']:
    print(topping)


favorite_languages ={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages)>1:
        print("\n"+ name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() +" 's favorite language is:")