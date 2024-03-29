#define a dictionary
todo_lists = {}
#function to create a new to-do list
def create_todo_list(name):
    if name not in todo_lists:
        todo_lists[name] = []
        print(f"To_do list '{name}'created successfully.")
    else:
        print(f"To_do list '{name}' already exists.")

#function to add task to a to-do list
def add_task(list_name,task):
    if list_name in todo_lists:
        todo_lists[list_name].append(task)
        print(f"Task '{task}' added to '{list_name}' list.")
    else:
        print(f"To_do list '{list_name}' does not exist.")

#function to view tasks in a to_do list
def view_tasks(list_name):
    if list_name in todo_lists:
        print(f"To_do list '{list_name}' :")
        for task in todo_lists[list_name]:
            print(f" - {task}")
    else:
        print(f"To_do list '{list_name}' does not exits.")

#main loop for user interaction
while True:
    print("\nCommands:")
    print("1.Create a new to_do list")
    print("2.Add a task to a to_do list")
    print("3.View tasks in a to_do list")
    print("4.Exit")

    choice = input("Enter your choice(1/2/3/4): ")

    if choice == "1":
        name = input("Enter the name of the new to_do list :")
        create_todo_list(name)
    elif choice == "2":
        list_name = input("Enter the name of the to_do list :")
        task = input("Enter the task to add :")
        add_task(list_name,task)
    elif choice == "3":
        list_name = input("Enter the name of the to_do list :")
        view_tasks(list_name)
    elif choice == "4":
        print("Existing from the to_do application . Goodbye!")
        break
    else:
        print("Invalid choice . plese choose a valid option.")

    