"""
1) Create a function named ds with parameters roll_no and name.
2) Add those parameters in the following data structures: list, tuple, sets and dictionaries
3) After adding values change the values during runtime
4) Delete these data structures
"""


def ds(roll_no, name):
    list = [roll_no, name]
    tuple = (roll_no, name)
    set = {roll_no, name}
    dict = {'roll_no': roll_no, 'name': name}

    print("\nBefore changing values")
    print("List: ", list)
    print("Tuple: ", tuple)
    print("Set: ", set)
    print("Dict: ", dict)

    new_name = input("enter new name: ")
    new_roll_no = int(input("enter new roll_no: "))

    list[0] = new_roll_no
    list[1] = new_name

    set.remove(roll_no)
    set.remove(name)
    set.add(new_roll_no)
    set.add(new_name)

    dict['name'] = new_name
    dict['roll_no'] = new_roll_no

    print("\nAfter changing values at runtime: ")
    print("List: ", list)
    print("Tuple: ", tuple)
    print("Set: ", set)
    print("Dict: ", dict)

    del list
    del tuple
    del set
    del dict

    print("data structures deleted")


ds(45, "Ayan")
