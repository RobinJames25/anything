import greet_people
from greet_people import build_person
from greet_people import build_person as bp
import greet_people as gt
from greet_people import *




musician= gt.build_person('jimi', 'hendrix','cooks')
musician=greet_people.build_person('jimi', 'hendrix','cooks')
musician=bp('jimi', 'hendrix','cooks')
musician=build_person('jimi', 'hendrix','cooks')
print(musician)