import random

payer = ["Anela", "Ben", "Charlie", "Diana"]

ranmdom_payer = random.randint(0,3)
print(ranmdom_payer)
print(f"{payer[ranmdom_payer]}, is going to pay the bill!!!")

#other function from random module
print(random.choice(payer))