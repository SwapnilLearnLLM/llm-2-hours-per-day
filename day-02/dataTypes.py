# Python Primitive Data Types
# String : "Swapnil"
# Subscripting
#Strings
print("HELLO"[4])
print("HELLO"[-1])
print("123" + "456")  # Concatenation

# Integer = Whole Numbers
print(123 + 456)
#Large Integers
print(123_456_789)

# Float = Floating point numbers (Decimal Numbers)
print(3.14159)

# Boolean = True or False
print(True)
print(False)

# Type Conversion/Type Casting
print(len("1234"))

# Anything inside "" is a string
# To know the type of data type use type(), it is called as type checking
print(type("Hello"))
print(type(123))
print(type(3.14))
print(type(True))

"123"   # String
int("123")  # Converts string to integer
print(int("123") + int("456"))
# int()
# float()
# str()
# bool()

#print("Number of letters in your name : " + str(len(input("What is your name "))))

name_of_user = input("What is your name ")     
lenght_of_name = len(name_of_user)
# print("Number of letters in your name : " + lenght_of_name) Type Error
print(type(lenght_of_name))
print(type("Number of letters in your name"))
print("Number of letters in your name : " + str(lenght_of_name))

# Mathematical Operations
print(3 + 5)  # Addition
print(7 - 4)  # Subtraction
print(3 * 2)  # Multiplication
print(6 / 3)  # Division
print(6//3) # Floor Division-> Int Type
print(2 ** 3)  # Exponentiation

#PEMDASLR
# LR Stands for Left to Right
# ()
# Exponentiation
# Multiplication and Division
# Addition and Subtraction
print(3 * 3 + 3 / 3 - 3) # 7.0
print(3 * (3 + 3) / 3 - 3) # 3.0

# Assignment variable
score = 0
# score = score + 1
# assignment vaiable can be used as below
score +=1
print(score)

# f strings
print(f"Your score is: " + str(score))

height = 1.8
is_winning = True

print(f"Your score is = {score} \nYour height is = {height} \nYou are winning is = {is_winning}")