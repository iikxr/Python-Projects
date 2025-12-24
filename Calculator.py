#Ask for user input

operation = int(input("What operation would you like to use? 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
num1 = float(input("What's your first number?: "))
num2 = float(input("What's your second number?: "))

x = num1 + num2
y = num1 - num2
z = num1 * num2
t = num1 / num2
#Setup calculations
if operation == 1:
    print(x)
elif operation == 2:
    print(y)
elif operation == 3:
    print (float(z))
elif operation == 4:
    print (float(t))
else:
    print ("Invalid Operation")