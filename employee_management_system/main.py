from AddEmployee import add
from ViewEmployee import view
from SearchEmployee import search
from DeleteEmployee import delete
from UpdateEmployee import update

def main():
    while True:
        print("\nWelcome to Employee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Update Employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            search()
        elif choice == '4':
            delete()
        elif choice == '5':
            update()
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
