import random
import hangman_art as art
import hangman_words as words
import os


chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(art.logo)

# Testing code
# print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
guesses = []
for _ in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system("cls")

    if guess in guesses:
        print(f"{guess} has already been tried, try another one.")
        print(f"{' '.join(display)}")
        print(art.stages[lives])
        continue
    else:
        guesses.append(guess)

    print(f"Guesses: {" ".join(guesses)}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f'too bad! "{guess}" is not in the word. Try Again.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. the word was {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(art.stages[lives])
    print("")
