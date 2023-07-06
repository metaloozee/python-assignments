def search():
    try:
        id_to_search = input("enter employee's id to search: ")
        with open('employees.txt', 'r') as f:
            employees = f.readlines()
            flag = False

            for employee in employees:
                name, id = employee.strip().split('-')
                if id == id_to_search:
                    print("\nEmployee Found: \n")
                    print(f"name: {name}, id: {id}")
                    flag = True
                    break
                if not flag:
                    print("employee not found")
    except Exception as e:
        print("an error occurred in search.py")