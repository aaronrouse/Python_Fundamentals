#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

import random
def randInt():
    num = random.random() *100
    return num
print(randInt())

import random
def randInt(max= 100):
    num = random.random() * 100
    return num
print(randInt())

import random
def randInt(min= 0):
    num = random.random() * 100
    return num
print(randInt())

import random
def randInt(min= 25, max= 75):
    num = random.random() * 25 + 50
    return num
print(randInt())