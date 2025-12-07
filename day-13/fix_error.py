try:
    age = int(input("How old are you?\n"))
except ValueError:
    print("Ypu have typed in an invalid number. Please try again with numerical value lik 15.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
