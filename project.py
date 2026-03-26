import random
import time

# Dictionary with keys (the answers) and the items (Definitions/hints)
words = {
    "lightning": "A shock from the sky",
    "monitor": "A computer screen",
    "window": "transparent material used in homes",
    "picture": "A moment frozen in time",
    "binary": "Values represented by 0s and 1s, used by computer systems.",
    "monochrome": "All one colour",
    "cafeteria": "Somewhere where you can eat",
    "simplistic": "In a simple style"
}

# Get the answer for the game from words at random
answer = random.choice(list(words))

# Grabs the hint/definition
for i in words.keys():
    if i == answer:
        print("Hint:", words.get(answer))
    else:
        continue

# Strips the answer to a word alone to prevent hassle later on
answerstrip = answer.strip("['")

# Puts each letter into a list to be used later on maybe
lst = []
for i in answerstrip:
    lst += i.split(",")

# Amount of lives/guesses the user has
lives = 10
alive = True
completed = False
# Track guessed letters
guessed_letters = set()
incorrectletters = set()


def update_display(answer, guessed_letters):
    return [letter if letter in guessed_letters else '_' for letter in answer]


# Print the initial underscores
print(''.join(update_display(answerstrip, guessed_letters)))

# user guess + checks for completion or failure + checks for more than one letter entered, probably not very efficient lmao
# I'm 100% going to cringe at this in 2 years time haha

while alive:
    guess = input("Guess a letter: ").lower()

    # Empty guess check
    if guess == "" or guess == " " or guess == "\t":
        print("You must enter a string")
        print(''.join(update_display(answerstrip, guessed_letters)))
        continue
    # Prevent little cheaters
    if len(guess) != 1:
        print("One letter at a time!")
        print(''.join(update_display(answerstrip, guessed_letters)))
        continue

    # Prevents stupidity
    if guess.lower() in guessed_letters or guess.lower() in incorrectletters:
        print("That has already been guessed!")
        print(''.join(update_display(answerstrip, guessed_letters)))
        continue

    # Prevent user from entering a number
    if guess.isdigit():
        print("You must enter words!")
        print(''.join(update_display(answerstrip, guessed_letters)))
        continue

    # Checks if the user guessed a letter correctly
    if guess.lower() in lst:
        print("That is a letter!")
        guessed_letters.add(guess.lower())


    # but if guess is incorrect, say that it was incorrect and remove a life.
    else:
        print("That's not a letter!")
        lives -= 1
        incorrectletters.add(guess)

    # checks if the game is over via defeat
    if lives == 0:
        print("You lost the game!")
        print("  _____")
        print("/     |")
        print("|     |")
        print("|     O")
        print("|    -|-")
        print("|     |")
        print("|    / \\")
        print("___")
        alive = False
    # checks if the game is over via victory (whey hey)
    if ''.join(update_display(answerstrip, guessed_letters)) == answerstrip:
        print("You win!")
        break

    # print the updated underscore hint after all code is executed, then print the incorrect letters in a clear manner
    print(''.join(update_display(answerstrip, guessed_letters)))
    if lives < 10:
        print(f"Incorrect letters: {str(incorrectletters).lstrip("{'").rstrip("'}").replace("'", '')}")

    # depending on the lives left, print the hangman.
    if lives == 9:
        print("___")
    elif lives == 8:
        print("/")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("___")
    elif lives == 7:
        print("  _____")
        print("/")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("___")
    elif lives == 6:
        print("  _____")
        print("/      |")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("___")
    elif lives == 5:
        print("  _____")
        print("/      |")
        print("|      |")
        print("|      O")
        print("|")
        print("|")
        print("|")
        print("___")
    elif lives == 4:
        print("  _____")
        print("/      |")
        print("|      |")
        print("|      O")
        print("|      |")
        print("|      |")
        print("|")
        print("___")
    elif lives == 3:
        print("  _____")
        print("/      |")
        print("|      |")
        print("|      O")
        print("|     -|")
        print("|      |")
        print("|")
        print("___")
    elif lives == 2:
        print("  _____")
        print("/      |")
        print("|      |")
        print("|      O")
        print("|     -|-")
        print("|      |")
        print("|")
        print("___")
    elif lives == 1:
        print("  _____")
        print("/      |")
        print("|      |")
        print("|      O")
        print("|     -|-")
        print("|      |")
        print("|     /")
        print("___")
# If not using an IDE, this helps see the result when using native python, QOL thing.
time.sleep(2)
