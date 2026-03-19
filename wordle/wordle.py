import random
import time

with open("words.txt") as f:
    words = f.read().splitlines()

wordle_words = [x for x in words if len(x) == 5]
random_wordle = random.choice(wordle_words)

print ("Welcome to Wordle!")
time.sleep(1)

while True:
    guess = input("Your Guess: ")
    if len(guess) == 5:
        break
    print("Invalid guess.")

for i in range(len(guess)):
    if guess[i] == random_wordle[i]:
        print ("Letter Correct")
    elif guess [i] in random_wordle:
        print ("Letter is in the word, but wrong spot")
    else:
        print("Letter not in the word.")