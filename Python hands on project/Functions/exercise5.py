# Make a list of magician’s names. Pass the list to a function 
# called show_magicians(), which prints the name of each magician in the list
magician_names = ['robin', 'dinamo', 'curt']

def show_magicians(magician_names):
    """Prints the names of magicians in the list."""
    
    for name in magician_names:
        print(name.title())
print("Original list of magicians.")
show_magicians(magician_names)

# Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to 
# see that the list has actually been modified.

def make_great(magician_names):
    """Adds 'the Great' to each magician's name."""
    great_magicians = []  # Create an empty list to store modified names
    for name in magician_names:
        great_magician = name + " the Great"
        great_magicians.append(great_magician)
    return great_magicians

#  Start with your work from Exercise 8-10. Call the 
# function make_great() with a copy of the list of magicians’ names. Because the 
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.

# Call make_great() with a copy of the original list
new_list = make_great(magician_names[:])

# Modified list
print("\nModified list of magicians:")
show_magicians(new_list)

