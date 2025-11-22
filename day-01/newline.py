#CONCATINATED STRINGS
print("Hello World!\nHello World!\nHello World!")

print("Hello" + "Angela") # Without Space

print("Hello" + " " + "Angela") # With Space

# Task3 Take input from User
#input("What is your name?")

# Take the name from user and greet them with hello
#print("HELLO" + " " + input("What is your name?"))

#Task 4 to add exclamation after the name
#print("Hello" + " " + input("What is your Name?") + "!")

# Python Variables, # Length of the name 
# name = input("What is your name? ")
#print(len(name))
# print(name + " " + "Length of name is " + str(len(name)))

# print(len(input("What is your name?")))

# Task 5 - Different Valiables
username = input("What is your name? ")
length = len(username)
print(length)


# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. 
# Write 3 lines of code to switch the contents of the variables. 
# You are not allowed to type the words "milk" or "juice". Y
# ou are only allowed to use variables to solve this exercise.
glass1 = "milk"
glass2 = "juice"
glass3 = glass1
glass1 = glass2
glass2 = glass3
print ("Glass1 now is:  " + glass1 + " " + "Glass2 now is: " + glass2)