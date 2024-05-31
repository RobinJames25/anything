# #  Using your latest Restaurant class, store it in a mod￾ule. Make a separate file that imports Restaurant. Make a Restaurant instance, 
# # and call one of Restaurant’s methods to show that the import statement is work￾ing properly

# from exercise3 import Restaurant

# ice_cream=Restaurant('am', 'dessert')
# ice_cream.describe_restaurant()

# # Start with your work from Exercise 9-8 (page 178).
# # Store the classes User, Privileges, and Admin in one module. Create a sepa￾rate file, make an Admin instance, and call show_privileges() to show that 
# # everything is working correctly

# from exercise3 import User,Privileges,Admin

# admin=Admin('robin','james',20,'kutus')
# admin.privileges.privileges_list=['can add post' , 'can delete post' , 'can ban user']
# admin.privileges.show_privileges()

# Store the User class in one module, and store the 
# Privileges and Admin classes in a separate module. In a separate file, create 
# an Admin instance and call show_privileges() to show that everything is still 
# working correctly

from privileges_admin import Admin

admin=Admin('robin','james',20,'kutus')
admin.privileges.privileges_list=['can add post' , 'can delete post' , 'can ban user']
admin.privileges.show_privileges()