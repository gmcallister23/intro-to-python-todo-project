task = []

def display_menu():
    print("Welcome to your To-Do List!")
    print("Please section an option:")
    print("1. Add New Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    new_task = input("What would you like ot add to your to-do list?")
    task.append(new_task)
    print(f"{new_task} has been added to your to-do list.")
    print(task)

def view_task():
    if len(task) == 0:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i in range(len(task)):
            print(f"{i+1}. {task[i]}")

def delete_task():
    for i, item in enumerate(task, 1):
        print(f"{i}. {item}")

    try:
        selection = int(input("Which task do you want to delete? "))
        if selection < 1 or selection > len(task):
            raise IndexError
        else:
            task.pop(selection - 1)
            print(task)
    
    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("That task number does not exist.")

    finally:
        print("Task deletion attempt complete.")
    
    