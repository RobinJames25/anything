#Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'
alien_color = 'green'
if alien_color == 'green':
    print("You have earned 5 points.")

alien_color='red'
if alien_color == "green":
    print("\nYou have earned 5 points.")

#If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
alien_color="red"
if alien_color == "green":
    print("You just earned 5 points for shooting the alien.")
#If the alien’s color isn’t green, print a statement that the player just earned 10 points.
if alien_color != "green":
    print("You just earned 10 points.")
#Write one version of this program that runs the if block and another that runs the else block.
alien_color="red"
if alien_color == "green":
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points.")
#Turn your if-else chain into an  if-elif-else chain.
alien_color="red"

if alien_color == "green":
    print("\nYou have earned 5 points.")
elif alien_color == "yellow":
    print("\nYou have earned 10 points.")
elif alien_color == "red":
    print("\nYou have earned 15 points.")

# Write an if-elif-else chain that determines a person’s stage of life.
age=  -5

if age < 2 and age > 0 :
    print("The age is fit for a baby.")
elif age>=2 and age < 4:
    print("The age is fit for a toddler.")
elif age>=4 and age < 13:
    print("The age is fit for a kid.")
elif age>=13 and age < 20:
    print("The age is fit for a teenager.")
elif age>=20 and age < 65:
    print("The age is fit for an adult.")
elif age>=65:
    print("The age is fit for a elder.")
else:
    print("The age is Invalid.")

# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list
fav_fruits=["apples","pineapples","mangoes","passion","banana"]
if "apples" in fav_fruits:
    print("\nYou really like apples")
if "pineapples" in fav_fruits:
    print("You rally like pineapples")
if "mangoes" in fav_fruits:
    print("You really like mangoes")
if "passion" in fav_fruits:
    print("You really like passion")
if "banana" in fav_fruits:
    print("You really like banana")