# Write a function that accepts a list of items a person wants 
# on a sandwich. The function should have one parameter that collects as many 
# items as the function call provides, and it should print a summary of the sand￾wich that is being ordered. Call the function three times, using a different num￾ber of arguments each time

def sandwich_toppings(*toppings):
    print('Adding the following toppings to sandwich: ')
    for topping in toppings:
        print('-'+topping.title())

sandwich_toppings('kales','tomatoes','meat')
sandwich_toppings('matke','nuts')

# Start with a copy of user_profile.py from page 153. Build 
# a profile of yourself by calling build_profile(), using your first and last names 
# and three other key-value pairs that describe you

def user_profile(first_name,last_name,**my_info):
    profile={}
    profile['firstname']=first_name.title()
    profile['lastname']=last_name.title()

    for key,value in my_info.items():
        profile[key]=value.title()

    return profile

my_profile=user_profile('robins', 'obiri',location='kanairo',career='software development')

print(my_profile)

#  Write a function that stores information about a car in a diction￾ary. The function should always receive a manufacturer and a model name. It 
# should then accept an arbitrary number of keyword arguments. Call the func￾tion with the required information and two other name-value pairs, such as a 
# color or an optional feature. Your function should work for a call like this one:
def make_car(manufacturer,model,**cars_info):
    car_desc={}
    car_desc['manufacturer']=manufacturer.title()
    car_desc['model']=model.title()

    for key,value in cars_info.items():
        car_desc[key]=value.title()

    return car_desc

final_info=make_car('toyota','cx5',color='black',size='suv')

print(final_info)