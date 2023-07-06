def view():
    try:
        with open("employees.txt", 'r') as f:
            employees = f.readlines()
            if (employees):
                print("\nEmployees: \n")
                for employee in employees:
                    name, id = employee.strip().split('-')
                    print(f"Name: {name}, ID: {id}")
            else:
                print("the database is empty")
    except Exception as e:
        print(f"an error occurred in view.py")