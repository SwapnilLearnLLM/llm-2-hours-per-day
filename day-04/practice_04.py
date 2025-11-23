import random


# random_integer = random.randint(1,10)
# print(random_integer)

# random floating point numbers
# random_number_0_to_1 = random.random() * 10# 0.0 to 1.0
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

# Heads or Tails Guess
random_guess = random.randint(0,1)

if random_guess == 0:
    print("Tails")
else:
    print("Heads")