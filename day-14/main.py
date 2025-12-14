import random
from art import logo
from art import vs
from game_data import data



def format_data(account):
    """With this piece of code we are formating the dictionary data into 
    printable format data which return the 
    string to provide the exact output we require."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """This will check the answer from the user if he has selected correct answer"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"  

print(logo)

score = 0

game_continue = True

account_b = random.choice(data)

while game_continue:


    account_a = account_b

    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    account_name = account_a["name"]
    account_desc = account_a["description"]
    account_country = account_a["country"]

    print(f"Compare A: {format_data(account_a)}")

    print(vs)

    print(f"Against B: {format_data(account_b)}")

    user_guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're Right! Your score is {score}")

    else:
        print(f"Sorry, you're wrong. Final score is {score}")
        game_continue = False