from pathlib import Path
from functions import get_todos, save_todos, get_valid_index

# Define the root directory of the project
ROOT_DIR = Path(__file__).resolve().parent
filename = ROOT_DIR / 'files' / 'todos.txt'

welcome_banner = """
████████╗ ██████╗ ██████╗  ██████╗     █████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗   ██╔══██╗██╔══██╗██╔══██╗
   ██║   ██║   ██║██║  ██║██║   ██║   ███████║██████╔╝██████╔╝
   ██║   ██║   ██║██║  ██║██║   ██║   ██╔══██║██╔═══╝ ██╔═══╝ 
   ██║   ╚██████╔╝██████╔╝╚██████╔╝   ██║  ██║██║     ██║     
   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝  ╚═╝╚═╝     ╚═╝     
"""

def main():
    print(welcome_banner)
    print("Welcome to the TODO App!")
    print("""
    Manage your tasks efficiently from the terminal.\n
    Add("1" or "add"), Show("2" or "show"), Edit("3" or "edit"), Complete("4" or "complete"), Exit("5" or "exit"):
    """)

    while True:
        user_input = input("Please enter your todo option: ")
        user_input = user_input.strip().title()
        match user_input:
            case '1' | 'Add':
                todos = get_todos(filename)
                new_todo = input("Enter a new todo item: ").strip()
                if not new_todo:
                    print("Cannot add an empty todo.")
                elif new_todo.lower() + '\n' in [t.lower() for t in todos]:
                    print("Todo item already exists.")
                else:
                    todos.append(new_todo + '\n')
                    save_todos(filename, todos)

            case '2' | 'Show':
                todos = get_todos(filename)
                if not todos:
                    print("No todos found.")
                else:
                    print("Todo List:")
                    for index, todo in enumerate(todos, start=1):
                        print(f"{index}. {todo.strip()}")

            case '3' | 'Edit':
                todos = get_todos(filename)
                index = get_valid_index(todos, "Enter which item number(starts with 1) you want to edit: ")
                if index is not None:
                    new_text = input("Enter the new todo item: ").strip()
                    if new_text:
                        todos[index] = new_text + '\n'
                        save_todos(filename, todos)
                    else:
                        print("Cannot update to an empty todo.")

            case '4' | 'Complete':
                todos = get_todos(filename)
                index = get_valid_index(todos, "Enter which item number(starts with 1) you want to mark complete: ")
                if index is not None:
                    todos.pop(index)
                    save_todos(filename, todos)
            case '5' | 'Exit':
                break

if __name__ == "__main__":
    main()
