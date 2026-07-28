import random

# List of words
words = [
    "apple",
    "mango",
    "banana",
    "python",
    "orange",
    "computer",
    "program",
    "keyboard",
    "monitor",
    "internet"
]

# Random word selection
word = random.choice(words)

# Display list
display = []

for letter in word:
    display.append("_")

# Number of lives
lives = 6

# Store guessed letters
guessed_letters = []

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

while lives > 0:

    print("\nWord :", " ".join(display))
    print("Guessed Letters :", " ".join(guessed_letters))
    print("Lives Remaining :", lives)

    guess = input("Enter a letter: ").lower()

    # Check single alphabet
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:

        for position in range(len(word)):
            if word[position] == guess:
                display[position] = guess

        print("Correct Guess!")

    else:
        lives -= 1
        print("Wrong Guess!")

    # Win condition
    if "_" not in display:
        print("\n==============================")
        print("Congratulations! You Won!")
        print("The Word is :", word)
        print("==============================")
        break

# Lose condition
if lives == 0:
    print("\n==============================")
    print("Game Over!")
    print("The Correct Word was :", word)
    print("==============================")
