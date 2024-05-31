#Defining a Function
def greet_user():
    """Display a simple greeting."""
    print("Hello")

greet_user()

#Passing Information to a Function
def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('Robin')
greet_user('Marrie')

#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = first_name + ' ' + last_name
 return full_name.title()

while True:
   print("\nPlease tell me your name:(enter 'q' at any time to quit)")
   f_name= input("First name: ")
   if f_name == 'q':
      break 

   l_name= input("Last name: ")
   if l_name == 'q':
      break
   
   formatted_name = get_formatted_name(f_name,l_name)
   print("\Hello, " + formatted_name + "!")
