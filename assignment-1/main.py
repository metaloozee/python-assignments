import requests

def arithmetic_operations():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        
        print("\nResults:")
        print(f"{num1} + {num2} = {addition}")
        print(f"{num1} - {num2} = {subtraction}")
        print(f"{num1} * {num2} = {multiplication}")
        print(f"{num1} / {num2} = {division}")
    except ValueError:
        print("Please enter valid numbers!")

def palindrome_checker():
    text = input("Enter a string to check if it's a palindrome: ")
    cleaned_text = ''.join(text.lower().split())
    result = cleaned_text == cleaned_text[::-1]
    print(result)

def file_handler():
    input_file = input("Enter input file name: ")
    output_file = input("Enter output file name: ")
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            word_count = len(content.split())
        
        with open(output_file, 'w') as file:
            file.write(f"Number of words in {input_file}: {word_count}")
        print(f"Word count: {word_count}")
    except FileNotFoundError:
        print("Input file not found")

class StudentManagement:
    def __init__(self):
        self.students = {}
    
    def create_student(self):
        try:
            roll = int(input("Enter roll number: "))
            if roll in self.students:
                print("Student with this roll number already exists")
                return
            
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grades_input = input("Enter grades (comma-separated): ")
            grades = [int(g.strip()) for g in grades_input.split(",")]
            
            self.students[roll] = {'name': name, 'age': age, 'grades': grades}
            print("Student added successfully")
        except ValueError:
            print("Please enter valid data!")
    
    def read_student(self):
        try:
            roll = int(input("Enter roll number to view: "))
            if roll in self.students:
                student = self.students[roll]
                print(f"\nStudent Details:")
                print(f"Roll No: {roll}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Grades: {student['grades']}")
            else:
                print("Student not found")
        except ValueError:
            print("Please enter a valid roll number!")
    
    def update_student(self):
        try:
            roll = int(input("Enter roll number to update: "))
            if roll not in self.students:
                print("Student not found")
                return
            
            current_student = self.students[roll]
            print("\nCurrent Student Details:")
            print(f"Roll No: {roll}")
            print(f"Name: {current_student['name']}")
            print(f"Age: {current_student['age']}")
            print(f"Grades: {current_student['grades']}")
            
            proceed = input("\nDo you want to update this student? (yes/no): ").lower()
            if proceed != 'yes':
                print("Update cancelled.")
                return
            
            name = input("Enter new name (press Enter to skip): ")
            age_input = input("Enter new age (press Enter to skip): ")
            grades_input = input("Enter new grades (comma-separated, press Enter to skip): ")
            
            if name:
                self.students[roll]['name'] = name
            if age_input:
                self.students[roll]['age'] = int(age_input)
            if grades_input:
                self.students[roll]['grades'] = [int(g.strip()) for g in grades_input.split(",")]
            
            print("\nStudent details after update:")
            print(f"Roll No: {roll}")
            print(f"Name: {self.students[roll]['name']}")
            print(f"Age: {self.students[roll]['age']}")
            print(f"Grades: {self.students[roll]['grades']}")
            print("Student updated successfully")
        except ValueError:
            print("Please enter valid data!")
    
    def delete_student(self):
        try:
            roll = int(input("Enter roll number to delete: "))
            if roll in self.students:
                del self.students[roll]
                print("Student deleted successfully")
            else:
                print("Student not found")
        except ValueError:
            print("Please enter a valid roll number!")
    
    def show_menu(self):
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. View Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Return to Main Menu")
            
            sub_choice = input("\nEnter your choice (1-5): ")
            
            if sub_choice == "1":
                self.create_student()
            elif sub_choice == "2":
                self.read_student()
            elif sub_choice == "3":
                self.update_student()
            elif sub_choice == "4":
                self.delete_student()
            elif sub_choice == "5":
                break
            else:
                print("Invalid choice!")

class Student:
    def __init__(self):
        try:
            self.roll = int(input("Enter roll number: "))
            self.name = input("Enter student name: ")
            self.age = int(input("Enter student age: "))
            grades_input = input("Enter grades (comma-separated): ")
            self.grades = [int(g.strip()) for g in grades_input.split(",")]
            
            self.display_details()
            print(f"Average Grade: {self.calculate_average():.2f}")
        except ValueError:
            print("Please enter valid data!")
    
    def display_details(self):
        print("\nStudent Details:")
        print(f"Roll No: {self.roll}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
    
    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

def get_random_quote():
    print("\nFetching a random quote...")
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()[0]
            print(f"\nQuote: {data['q']}")
            print(f"Author: {data['a']}")
        else:
            print("Failed to fetch quote")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    while True:
        print("\n=== Python Assignment Menu ===")
        print("1. Arithmetic Operations")
        print("2. Palindrome Checker")
        print("3. File Handling")
        print("4. Student Management System")
        print("5. Student Class Operations")
        print("6. Get Random Quote")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-6): ")
        
        if choice == "0":
            print("Thank you for using the program. Goodbye!")
            break
        elif choice == "1":
            arithmetic_operations()
        elif choice == "2":
            palindrome_checker()
        elif choice == "3":
            file_handler()
        elif choice == "4":
            sm = StudentManagement()
            sm.show_menu()
        elif choice == "5":
            Student()
        elif choice == "6":
            get_random_quote()
        else:
            print("Invalid choice! Please enter a number between 0 and 6.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
