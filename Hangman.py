import random


# Word list
words = ["laptop", "mouse", "keyboard", "desktop", "mobile"]

# Pick a random word
secret_word = random.choice(words)
secret_word = secret_word.lower()

# Game variables
guessed_letters = []
wrong_count = 0
max_wrong = 6

# Main game
print("\nWelcome to Hangman!\n\n")
print(f"The word has {len(secret_word)} letters")

while wrong_count < max_wrong:
    # Show word with blanks
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print("Word:", display)
    print("Wrong guesses left:", max_wrong - wrong_count)
    
    # Get guess
    guess = input("\nGuess a letter: ").lower().strip()

    # Validate guess
    if len(guess) != 1:
        print("Enter only one letter.")
        continue
    if not guess.isalpha():
        print("Enter a valid letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Add to guessed letters
    guessed_letters.append(guess)

    # Check if correct or wrong
    if guess in secret_word:
        print("Correct!")
    else:
        wrong_count = wrong_count + 1
        print("Wrong!")

    # Check if won
    won = True
    for letter in secret_word:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        print("\n 😄🎉You won! Word:", secret_word)
        break

# Game over
if wrong_count >= max_wrong:
    print("\n  😔Game Over! Word was:", secret_word)
