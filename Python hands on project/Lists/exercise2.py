#Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner
guests=['Jalla','Abdi','Raheem','James','Robin']
message=guests[0]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[1]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[2]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[3]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[4]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)
#. Add a print statement at the end of your program stating the name of the guest who can’t make it.
busy=guests[4]
print("To all it concerns, i heard that "+busy+" won't make it to dinner.")
guests.remove('Robin')
print(guests)
#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
guests.append('Mkuu')
print(guests)
#Print a second set of invitation messages, one for each person who is still in your list.
message=guests[0]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[1]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[2]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[3]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[4]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

# Add a printstatement to the end of your program informing people that you found a bigger dinner table
print('To '+ guests[0] + ' i found a bigger dinner table for you all. Thank you \n')

print('To '+ guests[1] + ' i found a bigger dinner table for you all. Thank you \n')

print('To '+ guests[2] + ' i found a bigger dinner table for you all. Thank you \n')

print('To '+ guests[3] + ' i found a bigger dinner table for you all. Thank you \n')

print('To '+ guests[4] + ' i found a bigger dinner table for you all. Thank you \n')

#Use insert() to add one new guest to the beginning of your list
guests.insert(0,'Omondi')

guests.insert(3,'Nyakundi')

guests.append('Babu')

#Print a new set of invitation messages, one for each person in your list.
message=guests[0]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[1]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[2]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[3]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[4]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[5]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[6]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[7]+ " I would like to invite you to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

# Add a new line that prints a message saying that you can invite only two people for dinner.
print('To '+ guests[0] + ' sorry for all inconveniences. My new dinner table can only accumulate 2 guests because of unavoidable reasons. Thank you \n')
print('To '+ guests[1] + ' sorry for all inconveniences. My new dinner table can only accumulate 2 guests because of unavoidable reasons. Thank you \n')
print('To '+ guests[2] + ' sorry for all inconveniences. My new dinner table can only accumulate 2 guests because of unavoidable reasons. Thank you \n')
print('To '+ guests[3] + ' sorry for all inconveniences. My new dinner table can only accumulate 2 guests because of unavoidable reasons. Thank you \n')
print('To '+ guests[4] + ' sorry for all inconveniences. My new dinner table can only accumulate 2 guests because of unavoidable reasons. Thank you \n')
print('To '+ guests[5] + ' sorry for all inconveniences. My new dinner table can only accumulate 2 guests because of unavoidable reasons. Thank you \n')
print('To '+ guests[6] + ' sorry for all inconveniences. My new dinner table can only accumulate 2 guests because of unavoidable reasons. Thank you \n')
print('To '+ guests[7] + ' sorry for all inconveniences. My new dinner table can only accumulate 2 guests because of unavoidable reasons. Thank you \n')


#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner
print("To "+ guests[0]+ " Sorry for your removal from the guest list. Thank you!\n")
removed_guest=guests.pop(0)


print("To "+ guests[0]+ " Sorry for your removal from the guest list. Thank you!\n")
removed_guest=guests.pop(0)

print("To "+ guests[0]+ " Sorry for your removal from the guest list. Thank you!\n")
removed_guest=guests.pop(0)

print("To "+ guests[0]+ " Sorry for your removal from the guest list. Thank you!\n")
removed_guest=guests.pop(0)

print("To "+ guests[0]+ " Sorry for your removal from the guest list. Thank you!\n")
removed_guest=guests.pop(0)

print("To "+ guests[0]+ " Sorry for your removal from the guest list. Thank you!\n")
removed_guest=guests.pop(0)


# #Print a message to each of the two people still on your list, letting them know they’re still invited.
message=guests[0]+ " I would like you to know you are still invited to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)

message=guests[1]+ "  I would like you to know you are still invited to dinner on 31 of April 2023. Please purpose to attend. Thank you.\n"
print(message)


# #Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
del guests[0]
print(guests)
del guests[0]
print(guests)
