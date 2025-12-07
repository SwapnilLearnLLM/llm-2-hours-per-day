enemies = 1

def increase_enemies():
    global enemies # ---> Use global and variable name if you want to manipulate global variable.
    enemies = 2
    print(f"Enemies inside the fucntion: {enemies}")

increase_enemies()
print(f"Enemies Outside the function: {enemies}")

# Local Scope it is within the function
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

# Global scope
player_health = 10
def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# There is no block scope in python
game_leve = 3
enemies = ["Skeleton", "Zombies", "Alien"]

if game_leve < 5:
    new_enemy = enemies[0]

print(new_enemy)