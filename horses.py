import random
import time

horse1 = {"name": "Alexander ", "odds": 2}
horse2 = {"name": "Thomas Phi Ho (single and ready to mingle🍆🏳️‍🌈)", "odds": 3}
horse3 = {"name": "Gary", "odds": 5}
horse4 = {"name": "Edwin", "odds": 8}

horses = [horse1, horse2, horse3, horse4]

print ("Welcome to the chud races!🐎")
time.sleep(1)

option = 1
balance = 100
for x in horses:
    print(f"{option}. {x['name']} - {x['odds']}x odds")
    option +=1

time.sleep(1.5)


while True:

    choice = input("Which horse would you like to bet on? (q to quit): ")
    if choice == "q":
        print(f"This was your final balance: {balance}")
        break
    choice = int(choice)
    if choice<1 or choice>4:
        print("not a horse")
        continue

    while True:
        print(f"Your current balance is {balance}$")
        time.sleep(0.75)

        bet = int(input("How much would you like to bet?: "))
        if bet<=0:
         print("bro u can't bet nothing")
         continue

        elif bet>balance:
         print("u broke u don't got that much")
         continue
        
        else:
            break
    
    chosen_horse = horses[choice - 1]
    
    random.shuffle(horses)


    print("The race is starting...")
    time.sleep(2)
    print("Racing.  ", end="\r", flush=True)
    time.sleep(1)
    print("Racing.. ", end="\r", flush=True)
    time.sleep(1)
    print("Racing...", end="\r", flush=True)
    time.sleep(2)
    print()

    rankings = 1
    print("Here are the race results🐎:")
    time.sleep(1.5)
    for x in horses:
       print (f"{rankings}. {x['name']}")
       rankings += 1
    time.sleep(1.5)

    if chosen_horse == horses[0]:
       print("Your horse got first! You won!")
       winnings = chosen_horse["odds"]*bet
       balance += winnings
       time.sleep(1)
       print (f"Your new balance is {balance}$")

    else:
       print("Your horse didn't get first... You lost!")
       balance -= bet
       time.sleep(1)
       print (f"Your new balance is {balance}$")

    if balance<= 0:
       print("your too broke brother")
       break