import random
from hangman_words import word_list
from hangman_art import stages, logo

# Set the initial number of lives
lives = 6

# Display game logo
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize the placeholder for the word to guess (e.g., "_ _ _")
placeholder = "_" * word_length
print("Word to guess: " + placeholder)

# Track the game state
game_over = False
# List to store correctly guessed letters
correct_letters = []

while not game_over:
    print(f"*************************** {lives}/6 LIVES LEFT ***************************")
    guess = input("Guess a letter: ").lower()

    # Check if the letter was already guessed
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'.")

    display = ""
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display += letter
            # Add only new correct letters to the list
            if letter not in correct_letters:
                correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

    # Reduce lives if the guessed letter is not in the word
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word.")

        if lives == 0:
            game_over = True
            print(f"***************************** IT WAS '{chosen_word.upper()}'! YOU LOSE *****************************")

    # Win condition: no underscores left in display
    if "_" not in display:
        game_over = True
        print("********************************* YOU WIN *********************************")

    # Show the current hangman stage
    print(stages[lives])
