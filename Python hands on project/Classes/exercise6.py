from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides

    def roll_dice(self):
        print("Rolling the dice:")
        i=0
        while i<10:
            x=randint(1,self.sides)

            print(x)
            i += 1
# Create a 6-sided die
six_sided_die= Die()

# #Roll the 6-sided die 10 times

six_sided_die.roll_dice()

#Create a 10-sided die
ten_sided_die=Die(10)

#Roll the 10-sided die 10 times
ten_sided_die.roll_dice()

#Create a 20-sided die
twenty_sided_die=Die(20)

#Roll the 20-sided die 10 times
twenty_sided_die.roll_dice()