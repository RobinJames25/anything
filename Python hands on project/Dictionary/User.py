user_0={
    'username':'eferni',
    'first':'enrico',
    'last':'ferni',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
#Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())

friends=['phil','sarah']
for name in favorite_languages.keys():
    print("\n"+name.title())

    if name in friends:
        print("Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!"
              )
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#Looping Through a Dictionary’s Keys in Order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for languages in favorite_languages.values():
    print(languages.title())

for languages in set(favorite_languages.values()):
    print(languages.title())
