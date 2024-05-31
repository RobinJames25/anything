import printing_functions as pf

unprinted_designs=['iphone case', 'robot pendant', 'dodecahedron']
completed_models=[]

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

#Preventing a Function from Modifying a List

pf.print_models(unprinted_designs[:], completed_models)

fav_books=['Python Crash Course', 'Cant hurt me']

while fav_books:

    current_books=fav_books[:].pop()
    print (current_books)

    break

print(fav_books)