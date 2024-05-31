#Write a function called city_country() that takes in the name 
#of a city and its country.
#Call your function with at least three city-country pairs, and print the value 
#that’s returned.
def city_country(city, country):
    
    name_city=city
    name_country=country

    full_details=name_city+", " +name_country

    return full_details.title()

my_country=city_country('nairobi', 'kenya')
print(my_country)
my_country=city_country('mombasa', 'kenya')
print(my_country)
my_country=city_country('kisumu','kenya')
print(my_country)

# Write a function called make_album() that builds a dictionary 
# describing a music album. The function should take in an artist name and an 
# album title, and it should return a dictionary containing these two pieces of 
# information. Use the function to make three dictionaries representing different 
# albums. Print each return value to show that the dictionaries are storing the 
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the 
# number of tracks on an album. If the calling line includes a value for the num￾ber of tracks, add that value to the album’s dictionary. Make at least one new 
# function call that includes the number of tracks on an album.
def make_album(artist_name,album_title,tracks=''):
    album_1={'Name':artist_name.title(),'title':album_title.title()}
    album_2={'Name':artist_name.title(),'title':album_title.title()}
    album_3={'Name':artist_name.title(),'title':album_title.title()}

    if tracks:
        album_1['tracks']=tracks
    if tracks:
        album_2['tracks']=tracks
    if tracks:
        album_3['tracks']=tracks
    
    return album_1,album_2,album_3

info=make_album('Mike','zootopia')
print(info)
info_2=make_album('Robin','james made it',21)
print(info_2)

# Write a while
# loop that allows users to enter an album’s artist and title. Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created. Be sure to include a quit value in the while loop
def make_album(artist_name,album_title,tracks=''):
    album_1={'Name':artist_name.title(),'title':album_title.title()}
    album_2={'Name':artist_name.title(),'title':album_title.title()}
    album_3={'Name':artist_name.title(),'title':album_title.title()}

    if tracks:
        album_1['tracks']=tracks
    if tracks:
        album_2['tracks']=tracks
    if tracks:
        album_3['tracks']=tracks
    
    return album_1,album_2,album_3

while True:
    print("\nPlease enter an artists album and title:(enter 'q' at any time to quit)")
    artist_name=input("Artist's name: ")
    album_title=input("Album's name: ")
    
    break
info=make_album(artist_name,album_title)
print(info)

   