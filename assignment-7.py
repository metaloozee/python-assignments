"""
1) Create a function with default parameter "file" storing the file path
2) Open the "file" in append mode
3) Use writelines() method to add your roll number, name, and class
4) Use readines() method to print your data in the prompt

Note: Use try...except block with suitable exception class
"""


def write_data(file="test.txt"):
    try:
        f = open(file, "a+")

        roll = int(input("enter your roll no: "))
        name = input("enter your name: ")
        cl = input("enter your class: ")

        f.writelines([f"roll no: {roll}, name: {name}, class: {cl}"])

        f.seek(0)
        data = f.readlines()

        for line in data:
            print(line)

    except IOError:
        print("an error occurred while accessing the file.")


write_data()
