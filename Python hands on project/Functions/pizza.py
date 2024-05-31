#Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print('- ' + str(topping))

#Mixing Positional and Arbitrary Arguments

def making_piza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print('\nMaking a ' + str(size) + '_inch pizza with the following toppings:')
    for topping in toppings:
     print('- ' + str(topping))


