"""
Create a calculator using all the operators available in arithmetic operators.
"""

while True:
    print("select an operation")
    print("1: addition")
    print("2: subtraction")
    print("3: multiplication")
    print("4: division")
    print("5: floor Division")
    print("6: modulo")
    print("7: exponent")
    print("8: exit")

    ch = int(input("enter your choice: "))

    if ch == 8:
        print("thank you for using my calculator")
        break
    
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))

    if ch == 1:
        res = a + b
    elif ch == 2:
        res = a - b
    elif ch == 3:
        res = a * b
    elif ch == 4:
        res = a / b
    elif ch == 5:
        res = a // b
    elif ch == 6:
        res = a % b
    elif ch == 6:
        res = a ** b
    else:
        print("invalid choice provided")
        continue

    print(f"result = {res}")