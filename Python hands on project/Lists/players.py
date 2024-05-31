#Slicing a List
players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#Looping Through a Slice
players=['charles','martina','michael','florence','eli']
print("Here is a list of the first three players on my team:")
for player in players[:3]:
    print(player.title())


