#  Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user
usernames=['ali','robin','james','admin','obiri','okioma']
for username in usernames:
#If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
    if username=='admin':
        print("Hello admin, would you like to see a status report?")
# print a generic greeting, such as Hello Eric, thank you for log￾ging in again
    else:
        print("Hello "+ username +" thank you for logging in again.")
