import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")   
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# for nrletters in letters:
#     for nr_symbols in symbols:
#         for nr_numbers in numbers:
#             password = []
#             appendletter = password.append(nrletters)
#             appendSymbol = password.append(nr_symbols)
#             appendNumber = password.append(nr_numbers)
# print(password)
# password = []
# for nrletters in range(0, nr_letters):
#     password.append(letters[random.randint(0, len(letters)-1)])
# print(password)
# for nr_symbols in range(0, nr_symbols):
#     password.append(symbols[random.randint(0, len(symbols)-1)])
# print(password)
# for nr_numbers in range(0, nr_numbers):
#     password.append(numbers[random.randint(0, len(numbers)-1)])
# print(password)
# for char in password:
#     print(char)

# TUtorial

# password = ""
# for char in range(1,nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char

# for char in range(1, nr_symbols + 1):
#     random_char = random.choice(symbols)
#     password += random_char
# for char in range(1, nr_numbers + 1):
#     random_char = random.choice(numbers)
#     password += random_char

# print(f"Your password is: {password}")

# Hard Level - Order of characters randomised:
password_list = []
for char in range(0,nr_letters):
    password_list += random.choice(letters)

for char in range(0, nr_symbols):
    password_list += random.choice(symbols)
for char in range(0, nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")