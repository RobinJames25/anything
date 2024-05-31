#  Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message.

def make_shirt(text,size="Large shirt size my preference"):
    print(text+size)


make_shirt(text=" I love python and ")

def make_shirt(size,text=" I love them all"):
    print(size+text)

make_shirt(size='Large, medium and small')


# Write a function called describe_city() that accepts the name of 
# a city and its country. The function should print a simple sentence, such as 
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the 
# default country

def describe_city(city,country="kenya"):
    print(city.title() + " is in " + country.title())

describe_city('nairobi')
describe_city('kisumu')
describe_city('mumbai','india')