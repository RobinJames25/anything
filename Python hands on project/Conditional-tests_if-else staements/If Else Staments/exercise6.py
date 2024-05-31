#Make a list of five or more usernames called current_users
current_users=['Manu','Menu','Minu','Monu','Munu']
#Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list
new_users=['MANU','MENU','idris','alba','chris']

#Loop through the new_users list to see if each new username has already been used
for new_user in new_users:
    if new_user.title() in current_users:
        print("You will have to enter a new username!")
    else:
        print("User name is available.")
