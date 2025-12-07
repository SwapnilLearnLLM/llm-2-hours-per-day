import random
from art import logo

print(logo)

print("Welcome to number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

def number_guess():
    level = input("Choose difficulty. Type 'easy' or 'hard' : ")
    random_number =  random.randint(1,100)
    if level == "easy":
        print("You have 10 attempts remaining to Guess the number.")
        chance_easy = 10
        while chance_easy > 0:
            guess = int(input("Make a guess: "))
            if guess == random_number:
                print(f"You Got it! The number was {random_number}")
                return
            elif guess < random_number:
                print("Too Low. \n Guess again!")
                chance_easy -= 1
                print(f"{chance_easy} Chances Left")
            elif guess > random_number:
                print("Too High!\n Guess again.")
                chance_easy -= 1
                print(f"{chance_easy} Chances Left")
            elif 0 > guess < 100:
                print("Number out of range.")
                chance_easy -= 1
                print(f"{chance_easy} Chances Left")
            else:
                print("Please enter a number")
    elif level == "hard":
        chance_easy = 5
        print("You have 5 attempts remaining to Guess the number.")
        while chance_easy > 0 :
            guess1 = int(input("Make a guess: "))
            if guess1 == random_number:
                print(f"You Got it! The number was {random_number}")
                return
            elif guess1 < random_number:
                print("Too Low. \n Guess again!")
                chance_easy -= 1
                print(f"{chance_easy} Chances Left")
            elif guess1 > random_number:
                print("Too High!\n Guess again.")
                chance_easy -= 1
                print(f"{chance_easy} Chances Left")
            else:
                print("Number out of range.")
                chance_easy -= 1
                print(f"{chance_easy} Chances Left")
        print(f"You could not guess the number. It was {random_number}")
    else:
        print("Wrong Choice!")
    
    #print (f"Correct Number was {random_number}")
number_guess()


