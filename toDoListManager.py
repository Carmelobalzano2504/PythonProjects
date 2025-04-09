def get_user_choice():
    user_input = str(input('What would you like to do: '))
    return user_input

def view_tasks():
    print(tasks)

def add_task():
    task = input('Enter a task: ')
    tasks.append(task)
    print(f'{task} added to the list!')

def delete_task():
    view_tasks()
    try:
        user_input = int(input('Choose index of task to delete: '))
        if 0 <= user_input < len(tasks):
            deleted_task = tasks.pop(user_input)
            print(f'Task "{deleted_task}" has been deleted!')
        else:
            print("Invalid index! Please select a valid task index.")
    except ValueError:
        print("Please enter a valid number.")

tasks = [] 

while True:
    print('Welcome to your to-do list!')
    print('1: Add a task')
    print('2: View a task')
    print('3: Delete a task')
    print('4: Exit')
    
    choice = get_user_choice()
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        break