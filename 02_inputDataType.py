# "input()" is a function that allows the user to input data from the keyboard
# Input always returns a string
#  And input is also used to read value from the terminale window. 

input("What is your name: ") # This will prompt the user to enter their name and return the value as a string

# Input values can be stored in a variable and then be used in the program
name = input("What is your name: ")
print(f"Hello {name}") # This is using the f-string ("f" in front of the string) to print the value of name

# Because input returns a string we can have something we call string concatinations
#  String Concatenation is the process of joining two or more strings together.
age = input("How old are you? ")
print("You are " + age + " years old") # This will concatenate the string "You are " with the value of age and the string " years old"


# Type Convertions
# Type conversion is the process of converting one data type to another.
#  For example, converting a string to an integer.
#  We can use the "int()" function to convert a string to an integer.
#  We can use the "float()" function to convert a string to a float.
#  We can use the "bool()" function to convert a string to a boolean.
#  We can use the "str()" function to convert a string to a string.
#  We can use the "list()" function to convert a string to a list.
#  We can use the "tuple()" function to convert a string to a tuple.
#  We can use the "dict()" function to convert a string to a dictionary.

# Example use case for type conversion:
# 1. Calculate how the year of birth of the user using the year 2026.
# Note: the input() function always returns a string, so we need to convert it to an integer using the int() function.
# It is after converting the value of the input() function into an integer that we can perform the arithmetic operation.
year = 2026
age = int(input("How old are you? ")) # the int() function will convert the value of the input() function into an integer
year_of_birth = year - age
print(f"You were born in {year_of_birth}")

# 2. Calculate the area of a triangle using the base and height.
base = float(input("Please provide the base length: "))
height = float(input("Please provide the height length: "))
area = (1 / 2) * (base * height)
print(f"The area of the triangle is {area}")

# What happens if you try to put 2 data types together?
print("Hello" + 18) # This will raise an error because you cannot concatenate a string and an integer
print("Hello" + str(18)) # This will work because we have converted the integer to a string
print("Hello" + "18") # This will work because we have converted the integer to a string
print("Hello" + "18") # This will work because we have converted the integer to a string
