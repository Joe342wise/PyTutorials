# If statements in python are used to make decisions in our programs.
# They allow us to execute different blocks of code depending on certain conditions.

#  example use case
temperature = 26

if temperature < 25:
    print("It's freezing!")
    print("Wear a jacket!")

# In the above example, the if statement checks if the temperature is less than 25 degrees.
# If it is, it prints "It's freezing!" and "Wear a jacket!" to the console.
# If the temperature is not less than 25 degrees, the if statement does nothing in the code block.  Therefore, nothing will be printed to the console.


# For situations where we know we will not be dealing with just one condition, we can use the else statement.
# The else statement is executed when the condition in the if statement is not met.

# example use case with else statement
age = 18
if age < 18:
    print("You are a child!")
else:
    print("You are an adult!")

# As the example illustrates, the else statement is executed when the condition in the if statement is not met.
# A more complex example could be as we rather take the input from the user rather than hardcoding a value.
score = int(input("Please enter your test score (0-100): "))

if score >= 90:
    print("Grade: A - Excellent work!")
elif score >= 80:
    print("Grade: B - Good job!")
elif score >= 70:
    print("Grade: C - Satisfactory")
elif score >= 60:
    print("Grade: D - Needs improvement")
else:
    print("Grade: F - Unfortunately, you failed.")

# You can realize from this example that there has been a new introdiction which is not "if" or "else"but "elif".
# elif is used to check multiple conditions in a single if statement.
# It is executed when the condition in the if statement is not met, and the condition in the elif statement is met.
# The elif statement is optional, and can be used multiple times in a single if statement.

# It doesn't just end here, there is something called the nested if statement.
# The nested if statement is used to check multiple conditions in a single if statement.
# An example usecase is as follows:
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"

if has_ticket:
    age = int(input("Please enter your age: "))
    if age < 18:
        print("You can enter for free!")
    else:
        print("Please proceed to pay the entrance fee.")
else:
    print("You cannot enter without a ticket.")
