class MyException(Exception):
    pass

class FileOperations:
    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        try:
            with open(self.filename, 'x') as file:
                print(f"{self.filename} created successfullt")
        except FileExistsError:
            print(f"error creating {self.filename}, the file might already exist")

    def read_file(self):
        with open(self.filename, 'r') as file:
            data = file.read()
        return data
    
    def write_file(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)
        return print(f"successfully inserted {data} into {self.filename}")
    
    def append_file(self, data):
        with open(self.filename, 'a') as file:
            file.write(data)
        return print(f"{data} successfully appended into {self.filename}")
    
    def raise_exception(self):
        raise MyException("user defined exception")
    
class StringOperations:
    def __init__(self, string):
        self.string = string
    
    def is_palindrome(self):
        self.string = self.string.lower()
        return self.string == self.string[::-1]
 
    def split_string(self):
        return self.string.split()
    
    def string_length(self):
        return len(self.string)

    def count_chars(self):
        unique_chars = set(self.string)
        return len(unique_chars)
    
    def rev_string(self):
        return self.string[::-1]
    
    def uppercase(self):
        return self.string.upper()
    
    def lowercase(self):
        return self.string.lower()
    
    def capitalize(self):
        return self.string.capitalize()
    
    def replace_substring(self, old_substr, new_substr):
        return self.string.replace(old_substr, new_substr)
    
    def raise_exception(self):
        raise MyException("user defined exception")
    

