usernames=[]
#If the list is empty, print the message We need to find some users!
if usernames:
    for username in usernames:
        if username=="admin":
            print("Hello admin would you like to see a report?")
        else:
            print("Hello "+username+" thank you for logging in.")
else:
    print("We need to find some users.")