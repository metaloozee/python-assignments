"""
Define any 3 variables with given marks or user-defined marks and calculate average. Display the average in following format:
The average of n1,n2 and n3 is ___
"""

a = int(input("enter n1: "))
b = int(input("enter n2: "))
c = int(input("enter n3: "))

avg = (a + b + c) / 3

print(f"The average of {a}, {b} and {c} is {avg}")