# Write a function called display_message() that prints one sen￾tence telling everyone what you are learning about in this chapter. Call the 
#function, and make sure the message displays correctly

def display_message():

    print("Hello everyone...I am learning about functions.")

display_message()

# Write a function called favorite_book() that accepts one 
# parameter, title. The function should print a message, such as One of my 
# favorite books is Alice in Wonderland. Call the function, making sure to 
# include a book title as an argument in the function call.

def favorite_book(title):
    print('One of my favorite books is ' + title.title())

favorite_book("can't break me-master your mind and defy the odds by David Goggins")