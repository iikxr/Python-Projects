# Ask for user input
expression = input("Enter your calculation (e.g., 24 + 4): ")

# Parse the expression
expression = expression.replace(" ", "")  # Remove spaces

# Find the operator
if "+" in expression:
    operator = "+"
    parts = expression.split("+")
elif "-" in expression:
    operator = "-"
    parts = expression.split("-")
elif "x" in expression or "*" in expression:
    operator = "x"
    expression = expression.replace("*", "x")
    parts = expression.split("x")
elif "/" in expression:
    operator = "/"
    parts = expression.split("/")
else:
    print("Invalid Operation")
    exit()

# Convert to numbers and calculate
num1 = float(parts[0])
num2 = float(parts[1])

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "x" or operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
