import random
import time

with open("words.txt") as f:
    words = f.read().splitlines()
# turned the opened file into a list with separate lines

wordle_words = [x for x in words if len(x) == 5]
random_wordle = random.choice(wordle_words)
# filtered words and selects a random 5 letter word from the list

print ("Welcome to Wordle!")
time.sleep(1)

attempts = 0
while True:
    guess = input("Your Guess: ")
    if len(guess) != 5:
         print("Invalid guess.")
         continue
    
    attempts +=1
# loops the input until a valid guess is given

    feedback = ""
    for i in range(len(guess)):
        if guess[i] == random_wordle[i]:
            feedback += (f"{guess[i]}🟢 ")
        elif guess [i] in random_wordle:
            feedback += (f"{guess[i]}🟡 ")
        else:
            feedback += (f"{guess[i]}🔴 ")
    print (feedback)

# word hint function, green yellow blank, basic wordle mechanic, feedback

    if guess == random_wordle:
        print ("Correct!")
        break

    if attempts == 6:
        print ("You ran out of attempts.")
        time.sleep(1)

        print (f"The word was: {random_wordle}!")
        break

    # game winning mechanic, detects attempt ammount and declares win/loss