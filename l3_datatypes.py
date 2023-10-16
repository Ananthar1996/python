##  String data type

## literal assignment of values
# first = "Dave"
# last = "Gray"

# print(type(first)) #string
# print(type(first) == str) #true
# print(isinstance(first, str)) #true

## constructor funtion

# pizza = str("Pepperoni")
# print(type(pizza)) #string
# print(type(pizza) == str) #true
# print(isinstance(pizza, str)) #true

## concatination

# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

## casting a number to a string

# decade = str(1980)
# print(type(decade))

# statement = "I like rock music from the " + decade + "s."
# print(statement)

##  mutiple lines

# multiline = ''' 
# Hey, how are you?                  

# I was just checking in.

#                                     All good?

# '''


# print(multiline)

# Escaping special characters (i\m-aposrphy, \t-tab space, \n-new line)
# sentence = 'I\'m back at work! \tHey!\n\nWhere\'s this at\\located' 
# print(sentence)

## string Methods 

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))
# multiline += "                                                        "
# multiline = "                " + multiline
# print(len(multiline))

# print(len(multiline.strip())) # strip removes whitespace
# print(len(multiline.lstrip())) # strip removes on left whitespace
# print(len(multiline.rstrip()))  # strip removes on right whitespace

## Build a menu

# title = "menu".upper() 
# print(title.center(20, "="))
# print("Coffe".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

## string index values

# print(first[0])
# print(first[1])
# print(first[2: -1])
# print(first[1:])

## some methods return boolean data

# print(first.startswith("D")) 
# print(first.endswith("V")) 

#  boolean data type

# myvalue = True # capitla T or F
# x = bool(False) # constructor
# print(type(x))
# print(isinstance(myvalue, bool))

#  numeric data types
# integer type

# price = 100
# best_price = int(80)

# print(type(price))
# print(isinstance(best_price, int))

# #  float type
gpa = 3.28
# y = float(1.14)
# print(type(gpa))
# print(isinstance(gpa, int))

# # complex type used in electrical enginnering
# print("")

# comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# # built in functions for numbers

# print(abs(gpa))
# print(abs(gpa * -1))
# print(round(gpa))
# print(round(gpa, 1))

## modules for math

import math 

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

## Casting a string to a number
zipcode = "10001"
zip_value=int(zipcode)
print(type(zip_value))
print(zip_value)





