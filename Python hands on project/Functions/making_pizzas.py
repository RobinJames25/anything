#Storing Your Functions in Modules
#Importing an Entire Module
import pizza

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

pizza.making_piza(12, 'mushrooms', 'green peppers', 'extra cheese')


#Importing Specific Functions

from pizza import make_pizza,making_piza

make_pizza('mushrooms', 'green peppers', 'extra cheese')
making_piza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to Give a Function an Alias
from pizza import making_piza as mp

mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to Give a Module an Alias
import pizza as p

p.make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Importing All Functions in a Module

from pizza import *

make_pizza('mushrooms', 'green peppers', 'extra cheese')
making_piza(12, 'mushrooms', 'green peppers', 'extra cheese')