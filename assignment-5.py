"""
Take input from the user of 5 numbers and store it in a list.
Perform below operations:

1) Calculate the sum of all the elements in the list
2) Find the smallest number
3) Find the largest number
4) Display list in ascending order
5) Display list in descending order
6) Convert list into tuple
7) Delete the list
"""

list = []
for i in range(5):
    num = int(input(f"enter number {i+1}: "))
    list.append(num)

print(f"sum of all elements in the list: {sum(list)}")

print(f"smallest number in the list: {min(list)}")

print(f"largest number in the list: {max(list)}")

list.sort()
print(f"list in ascending order: {list}")

list.reverse()
print(f"list in descending order: {list}")

print(f"list in sorted order: {tuple(list)}")

del list
print("list deleted")
