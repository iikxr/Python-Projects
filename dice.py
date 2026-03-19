import random
import time

while True:
    user_answer = input("Would you like to roll the dice? (Yes or No): ")

    if user_answer.lower() == ('yes'):
            print("Rolling...")
            time.sleep(1)
            print (random.randint(1, 6))
            time.sleep(1)

            while True:
                reroll = input("Would you like to roll again? (Yes/No): ")
                if reroll.lower() == ('yes'):
                    continue
                elif reroll.lower() == ('no'):
                    print ("Exiting...")
                    time.sleep(0.5)
                    exit()
                else:
                    print ("Invalid input.")

    elif user_answer.lower() == ('no'):
        print ("Exiting...")
        time.sleep(0.5)
        exit()
    else:
        print ("Invalid input.")




