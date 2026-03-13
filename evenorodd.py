import time

def question():
    print ("Welcome! Today, we'll see if your number is even or odd!")
time.sleep (1.5)
number = int(input("What's your number?: "))

time.sleep(1)
print ("Generating...")

if number % 2 == 0:
    time.sleep(1)
    print ("It's Even! Who would've guessed?")
else:
    time.sleep(1)
    print ("It's Odd! You wish it was even don't you?")

time.sleep(2)
if number % 2 != 0:
    choice = input("Don't you? Yes or No.")
else:
    exit()

time.sleep(1)
if choice.lower() == "yes":
    print ("You better.")
elif choice.lower() == "no":
    print ("How dare you.")
else:
    print ("Not how you answer.")
