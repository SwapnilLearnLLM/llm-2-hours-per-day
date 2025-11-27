import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)



chosen_word = random.choice(word_list)
# print(chosen_word)
word_length = len(chosen_word)
placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)
# while word_length > 0: I have donw it through while loop
#     print("_", end=" ")
#     word_length -=1

game_over = False

correct_guesses = []

lives = 6

while not game_over:
    guess_word = input("\nGuess a letter from the word:").lower()

    if guess_word in correct_guesses:
        print(f"You have already guessed the letter {guess_word}. Try another letter.")

    display = ""
    # Below code will replce the place holder if the word in correct

    for letter in chosen_word:
        if letter == guess_word:
            display += letter
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    print(display)

    if guess_word not in chosen_word:
        lives -= 1
        print(f"You guessed {guess_word}, that's not in the word. You lose a life.")
        print(f"*************You have {lives}/6 lives left.******************")
        if lives == 0:
            game_over = True
            print(f"*************It was {chosen_word}!You lose.******************")

    if "_" not in display:
        game_over = True
        print(f"******************You win!*****************")
    print(stages[6 - lives])

# print(chosen_word[0])
i = 0
# for guess_word in chosen_word:
# while i < len(chosen_word): I have done it through while loop
#     if guess_word == chosen_word[i]:
#         print(guess_word)
#         print(chosen_word[i])
#         print("Right")
#         i +=1
#     else:
#         print(guess_word)
#         print(chosen_word[i])
#         print("Wrong")
#         i += 1
# for letter in chosen_word:
#     if letter == guess_word:
#         print(letter)
#         print("Right")
#     else:
#         print(letter)
#         print("Wrong")