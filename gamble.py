import random
import time

slots  = ["🍒", "🍒", "🍒", "🍋", "🍋", "⭐", "7", "BAR"]


balance = 100

payouts = {
    "777": 10,
    "BAR": 5,
    "three": 3,
    "two": 1.5,
}

def match(reel1, reel2, reel3, amount):
        if reel1 == reel2 == reel3 == "7":
            return amount * payouts["777"]
        elif reel1 == reel2 == reel3 == "BAR":
            return amount * payouts["BAR"]
        elif reel1 == reel2 == reel3:
            return amount * payouts["three"]
        elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
            return amount * payouts["two"]
        else:
            return 0
        
while True:
    print (f"Your balance is: {balance}$")
    amount = int(input("How much would you like to bet?: "))
    if amount <= 0:
        print ("You can't bet nothing!")
        continue
    if amount > balance:
        print ("You can't bet more than you have!")
        continue

    reel1 = random.choice(slots)
    reel2 = random.choice(slots)
    reel3 = random.choice(slots)

    print (f"| {reel1} | {reel2} | {reel3} |")
    time.sleep(1)
    print ("Calculating your wins/losses...")
    time.sleep(1)




    winnings = match(reel1, reel2, reel3, amount)



    if winnings > 0:
        balance += winnings
        print(f"You won {int(winnings)}$!")
    else:
        balance -= amount
        print("You lost!")


    print (f"Your updated balance is {balance}$")



    if balance == 0:
        print ("You ran out of money! Yo u suck at gambling 😭😭😭🤣🤣💔💔💰💰💰")
        time.sleep(1)
        break