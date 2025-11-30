# Ceaser Cipher Program
from art import logo

print(logo)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


        
# def encrypt(original_text, shift_amountt):
#     encrypted_text = ""
#     for char in original_text:
#         position = alphabet.index(char)
#         new_position = position + shift_amount
#         new_position = new_position % len(alphabet)
#         encrypted_text += alphabet[new_position]
#     print(f"The encoded text is {encrypted_text}")

# def decrypt(original_text, shift_amountt):
#     decrypted_text = ""
#     for char in original_text:
#         position = alphabet.index(char)
#         new_position = position - shift_amount
#         new_position = new_position % len(alphabet)
#         decrypted_text += alphabet[new_position]
#     print(f"The decoded text is {decrypted_text}")

# if direction == "encode":
#     encrypt(original_text, shift_amount)
# elif direction == "decode":
#     decrypt(original_text, shift_amount)
# else:
#     print("Invalid Input")

def caesar(original_text, shift_amount, direction):
    result_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in original_text:
        if char not in alphabet:
            result_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_position = new_position % len(alphabet)
            result_text += alphabet[new_position]
    print(f"The {direction}d text is {result_text}")

should_continue = True

while should_continue:

    direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    original_text = input("Enter the text to encode/decode:\n").lower()

    shift_amount = int(input("Enter the shift number:\n"))

    caesar(original_text, shift_amount, direction)

    input_continue = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
    if input_continue == "no":
        should_continue = False
        print("Goodbye")