print("Hello World")

name= "Aaron"
print ("hello", name)

name = "Aaron"
print("Hello " + name + "!")

name = 7
print("Hello", name,"!")

name = 7
# print("Hello " + name + "!") #Printed out this error: TypeError: can only concatenate str (not "int") to str
print("Hello " + str(name) + "!")  #by adding str() it changed the integer to a string.

fave_food1 = "pizza"
fave_food2 = "cheeseburgers"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}.")

print("i love to eat pizza and cheeseburgers".islower())