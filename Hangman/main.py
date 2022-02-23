import hangman_art
import hangman_words
import random
import os

print(hangman_art.logo)
choose = input("Choose an alphabet you want. :").lower()
chosen_word = random.choice(hangman_words.alphabet[choose])  # or from hangman_words import word_list 후 hangman_words.을 제외할 수도 있다

display = []
for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False
lives = 6
guessed_letter = []

while not end_of_game:
    print(guessed_letter)
    did_match = False
    already_guessed = False
    guess = input("Guess a letter : ").lower()
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        os.system('cls')
    else:
        os.system('clear')

    for point in range(len(chosen_word)):
        if guess not in guessed_letter and guess == chosen_word[point]:
            display[point] = guess
            print(hangman_art.stages[lives])
            did_match = True
        elif guess in guessed_letter and guess == chosen_word[point]:
            print(f"{guess} is already guessed letter!")
            print(hangman_art.stages[lives])
            already_guessed = True
            did_match = True

    guessed_letter.append(guess)
    if already_guessed == False and did_match == False:
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The solution is : {chosen_word}")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

