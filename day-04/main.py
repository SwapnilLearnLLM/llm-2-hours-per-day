import random

rock = '''
    _______ 
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)
print(f"You chose:\n{game_images[choice]}")
print(f"Computer chose:\n{game_images[computer_choice]}")

if game_images[choice] == game_images[computer_choice]:
    print("It's a draw")
elif (game_images[choice] == rock and game_images[computer_choice] == scissors) or (game_images[choice] == paper and game_images[computer_choice] == rock) \
        or (game_images[choice] == scissors and game_images[computer_choice] == paper):
    print("You win!")
else:
    print("You lose!")