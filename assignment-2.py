"""
Demonstrate the use of all types of operators.
"""

# arithmetic operators
n1 = int(input("enter the value for n1: "))
n2 = int(input("enter the value for n2: "))
print("arithmetic operators:")
print("addition: ", n1 + n2)
print("subtraction: ", n1 - n2)
print("multiplication: ", n1 * n2)
print("division: ", n1 / n2)
print("floor division: ", n1 // n2)
print("modulus: ", n1 % n2)
print("exponential: ", n1 ** n2)

# assignment operators
print("\n\nassignment operators:")
a = 10
a += 5
print(a)
a = 10
a -= 5
print(a)
a *= 1
print(a)
a = 10
a /= 1
print(a)
a = 10
a **= 1
print(a)
a = 10
a //= 1
print(a)
a %= 1
print(a)

# Comparison operators
a = int(input("enter value for a: "))
b = int(input("enter value for b: "))
print("\n\ncomparison operators:")
print("'a > b: ", a > b)
print("a < b: ", a < b)
print("a >= b: ", a >= b)
print("'a <= b: ", a <= b)
print("a == b: ", a == b)
print("a != b: ", a != b)

# logical operators
print("\n\nlogical operators:")
x = False
y = True
print("x and y: ", x and y)
print("x or y: ", x or y)
print("not x: ", not x)

# Bitwise operators
p = 10
q = 20
print("\n\nbitwise operators:")
print("a | b: ", a | b)
print("a & b: ", a & b)
print("a ^ b: ", a ^ b)
print("a << b: ", a << b)
print("'a >> b: ", a >> b)

# Identity operator
print("\n\nidentity operators:")
r = 15
s = 20
print("r is s: ", a is b)
print("r is not s: ", a is not b)

# Membership operator
print("\n\nmembership operators:")
c = "ayan"
print("a" in c)
print("x" not in c)
