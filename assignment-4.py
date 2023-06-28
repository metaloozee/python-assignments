"""
Demonstrate the use of loop manipulation statements.
(break, pass, continue, for with else and while with else)
"""

numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    if n == 2:
        pass
    elif n == 4:
        break
    elif n == 6:
        continue
    print(n)
else:
    print("end of for loop with pass, break, continue, else")

count = 1
while count < 5:
    count += 1
else:
    print("end of while loop else")


