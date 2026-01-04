import random

rnumber = random.randint(1, 100)

print ("Welcome! Guess the random number between 1-100!")

while True:
    guess = int(input("What is your guess?: "))

    if guess < 1 or guess > 100:
        print ("Not valid number in range!")
    elif guess < rnumber:
       print ("Higher!")
    elif guess > rnumber:
        print ("Lower!")
    else:
        print ("Correct!")
        break