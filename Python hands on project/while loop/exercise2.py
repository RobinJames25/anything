# A movie theater charges different ticket prices depending on 
# a person’s age. If a person is under the age of 3, the ticket is free; if they are 
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
# $15. Write a loop in which you ask users their age, and then tell them the cost 
# of their movie ticket.



while True:
    age = input("Enter your age (or press 0 to exit): ")
    age=int(age)

    if age == 0:
        print("Thank you for visiting us.Come again!")
        break
    if age <= 3 and age >0:
        print("The ticket is free.")

    elif age >3 and age <=12:
        print("The ticket is $10")

    elif age >12:
        print("The ticket is 15$")

    else:
        print("Incorrect input!Please try again!")
        