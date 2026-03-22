"""
Arithmetic Operators
Arithmetic operators are used to perform mathematical operations on variables and values.
+ - * / % ** // are the arithmetic operators.
+ is the addition operator.
- is the subtraction operator.
* is the multiplication operator.
/ is the division operator.
% is the modulus operator.
** is the exponentiation operator.
// is the floor division operator. 
"""

# Example use case for arithmetic operators:
print(10 + 5) # This will add the value of 10 and 5 and print the result
print(10 - 5) # This will subtract the value of 10 and 5 and print the result
print(10 * 5) # This will multiply the value of 10 and 5 and print the result
print(10 / 5) # This will divide the value of 10 and 5 and print the result as a floating number
print(10 % 5) # This will return the remainder of the division of 10 and 5 and print the result
print(10 ** 5) # This will raise 10 to the power of 5 and print the result
print(10 // 5) # This will divide the value of 10 and 5 and print the result as an integer without decimals

"*******************************************************************************************************************"

"""
Augumented Assignment Operators
=, += -= *= /= %= **= //= are the augumented assignment operators.
= is the assignment operator.
+= is the augumented addition operator.
-= is the augumented subtraction operator.
*= is the augumented multiplication operator.
/= is the augumented division operator.
%= is the augumented modulus operator.
**= is the augumented exponentiation operator.
//= is the augumented floor division operator.
For all the arithmetic operators, we can use the augumented assignment operators to assign the result of the arithmetic operation to the variable.
"""

# For example:
x = 10
x = x + 5 # This will add the value of 10 and 5 and assign the result to the variable x
x += 5 # This will add the value of 10 and 5 and assign the result to the variable x
print(x) # This will print the value of x which is 15
"""
You can realize from the above examples that you will achive the same result with which ever approach you use.
But the augumented assignment operators are more efficient and concise.
So, it is recommended to use the augumented assignment operators whenever possible.
"""

y = 10
y *= 5 # This will multiply the value of 10 and 5 and assign the result to the variable x
print(y) # This will print the value of x which is 50

z = 10
z /= 5 # This will divide the value of 10 and 5 and assign the result to the variable x
print(z) # This will print the value of x which is 2

i = 10
i %= 5 # This will return the remainder of the division of 10 and 5 and assign the result to the variable x
print(i) # This will print the value of x which is 0

"*******************************************************************************************************************"

"""
Comparison Operators
Comparison operators are used to compare two values and return a boolean value.
== is the equality operator.
!= is the inequality operator.
> is the greater than operator.
< is the less than operator.
>= is the greater than or equal to operator.
<= is the less than or equal to operator.
"""

# For example:
x = 10
y = 5
print(x == y) # This will return False because 10 is not equal to 5
print(x != y) # This will return True because 10 is not equal to 5
print(x > y) # This will return True because 10 is greater than 5
print(x < y) # This will return False because 10 is not less than 5
print(x >= y) # This will return True because 10 is greater than or equal to 5
print(x <= y) # This will return False because 10 is not less than or equal to 5

"""
Note that "=" is not the same as "==".
"=" is the assignment operator.
"==" is the equality operator.
"""
# For example:
x = 10
y = 5
print(x = y) # This will return False because 10 is not equal to 5
print(x == y) # This will return True because 10 is equal to 5

"*******************************************************************************************************************"

"""
Logical Operators
Logical operators are used to build complex rules in conditions.
They always return a boolean value

We have the three main operators as:
and, or, not.
"""

# For example:
price = 100
quantity = 5
print(price > 50 and quantity > 3) # This will return True because both conditions are true
print(price > 50 or quantity > 3) # This will return True because at least one of the conditions is true
print(not price > 50) # This will return False because the condition is true and we are negating it with the not operator

"""
When to use the various logical operators:
- Use "and" when you want to check if multiple conditions are true at the same time.
- Use "or" when you want to check if at least one of the conditions is true.
- Use "not" when you want to negate a condition.

Therefore, you should note that;
- "and" will return True only if both conditions are true.
- "or" will return True if at least one of the conditions is true.
- "not" will return True if the condition is false and False if the condition is true
"""
