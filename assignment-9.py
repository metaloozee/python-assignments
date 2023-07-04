"""
1) Create a module consisting of class holding various data members and member functions.
(class can be on various file operations or mathematical operations or string operations)
2) Import the above module created and try to implement their member functions.
3) Also in the same file, create a user defined exception and implement it.

Note:
file operations should include all the file modes
mathematical operations should include the functions from math module
string operations should include string functions such as split()..etc
"""

from operations import FileOperations, StringOperations, MyException

# File operations
file_op = FileOperations("test.txt")
file_op.create_file()
file_op.write_file("Hello World")
print(f"data inside the created file: {file_op.read_file()}")
file_op.append_file("wassup")

print()

# String operations
str = input("enter a string: ")
string_op = StringOperations(str)
if string_op.is_palindrome() == True:
    print("the string is palindrome")
else:
    print("the string is not palindrome")
print(f"splitted string: {string_op.split_string()}")
print(f"length of the string is: {string_op.string_length()}")
print(f"number of unique characters in the string: {string_op.count_chars()}")
print(f"reversed string: {string_op.rev_string()}")
print(f"string uppercase: {string_op.uppercase()}")
print(f"string lowercase: {string_op.lowercase()}")
print(f"capitalized string: {string_op.capitalize()}")

old_substr = input("enter a substring which you want to replace: ")
new_substr = input(f"enter a new substring to replace with {old_substr}: ")
replaced_string = string_op.replace_substring(old_substr, new_substr)
print(f"replacing world with ayan: {replaced_string}")

print()

try:
    string_op.raise_exception()
except MyException as excp:
    print(excp)
