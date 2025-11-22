print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You' re at a cross road. Where do you want to go?\n \t Type 'left' or 'right'\n")
if direction.lower() == "right":
    print("Sorry, you fell into hole. Game Over")
elif direction.lower() == "left":
    choice = input("You' ve come to a lake. There is an island in middle of thr lake. \n Type 'wait' to wait for aboat. Type 'swim' to swim across.\n")
    if choice.lower() == "swim":
        print("You' ve been attacked. GAME OVER.")
    elif choice.lower() == "wait":
        door = input("You have arrived at the island. There is a house with 3 doors. one red, one yellow, one blue. Which colour do you choose?\n")
        if door.lower() == "red":
            print("It's a room full of fire. GAME OVER.")
        elif door.lower() == "blue":
            print("You enter a room of beasts. GAME OVER.")
        elif door.lower() == "yellow":
            print("You found the treasure! YOU WIN!")
        else:
            print("You chose a door that doesn't exist. GAME OVER.")
    else:
        print("Invalid choice. GAME OVER.")