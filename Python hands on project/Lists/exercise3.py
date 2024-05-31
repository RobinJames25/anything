#Think of at least five places in the world you’d like to visit.Store the locations in a list. Make sure the list is not in alphabetical order
places_to_visit=['Rio', 'Amsterdam','Paris','Toronto','GreatWall']
#Print your list in its original order
print(places_to_visit)
#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(places_to_visit))
#Use reverse() to change the order of your list. 
places_to_visit.reverse()
print(places_to_visit)
#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places_to_visit.reverse()
print(places_to_visit)
#Use sort() to change your list so it’s stored in alphabetical order.
places_to_visit.sort()
print(places_to_visit)
#Use sort() to change your list so it’s stored in reverse alphabetical order
places_to_visit.sort(reverse=True)
print(places_to_visit)
# use len() to print a message indicating the number of people you are inviting to dinner
guests=['Jalla','Abdi','Raheem','James','Robin']
number=len(guests)
print('The total number of people invited to dinner is ' + str(number))
#Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or any￾thing else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once
anime=['jjk','One piece','Aot','solo levelling','Ninja Kamui']
anime.sort()
print(anime)
anime.sort(reverse=True)
print(anime)
print(sorted(anime))
anime.reverse()
print(anime)
print(len(anime))