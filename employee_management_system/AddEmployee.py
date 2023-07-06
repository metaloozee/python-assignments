def add():
    try:
        with open('employees.txt', 'a') as f:
            name = input("enter employee's name: ")
            id = input("enter employee's id: ")
            
            f.write(f"{name}-{id}\n")
            print("successfully added an employee")
    except Exception as e:
        print("an error occurred in add.py")