import time
import random

print ("Welcome to Hangman!")
time.sleep (1)

with open("mediumwords.txt") as f:
    words = f.read().splitlines()

hangman_word = random.choice(words)

display = ["_"] * len(hangman_word)
print (" ".join(display))

guessed = []
wrong_guess = 0

while True:
    guess = input("Guess a letter!: ")
    if len(guess) != 1:
        print ("Only 1 letter!")
        continue

    if guess in guessed:
        print ("Letter already guessed!")
        continue

    if guess not in hangman_word:
        wrong_guess += 1
        print(f"Not a letter! {10 - wrong_guess} guesses left!")
        
    for i in range(len(hangman_word)):
        if hangman_word[i] == guess:
            display[i] = guess
    print (" ".join(display))

    guessed.append(guess)

    if wrong_guess == 10:
        print ("You lost the game!")
        time.sleep(1)
        print (f"The word was {hangman_word}!")
        break
