import glob
import csv
import shutil

def get_todos(filepath):
    """Reads todos from the file. Returns an empty list if file not found."""
    extension = str(filepath).split(".")[1]
    # Examples showing glob module usage
    myfiles = glob.glob("files/*."+extension)
    print("These text files are present inside files directory: \n",myfiles)
    try:
        with open(filepath, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_todos(filepath, todos_list):
    """Writes the list of todos to the file, creating the directory if it doesn't exist."""
    # Ensure the parent directory exists before writing the file
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as file:
        file.writelines(todos_list)

def get_valid_index(todos, prompt):
    """Prompts user for an index and validates it against the list."""
    try:
        index = int(input(prompt))
        if 1 <= index <= len(todos):
            return index - 1
        print(f"Item number {index} is not present.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None

def get_command_count(command):
    # Examples showing csv module usage
    with open('files/command.csv', 'r') as file:
        data = list(csv.reader(file))
    for row in data[1:]:
        if row[0].lower() == command.lower():
            return row[1]
    return None

def update_command_count(command, new_count):
    with open('files/command.csv', 'r') as file:
        data = list(csv.reader(file))

    # Flag to check if the command was found
    command_found = False

    for row in data[1:]:
        if row[0].lower() == command.lower():
            row[1] = new_count
            command_found = True
            break
    with open('files/command.csv', 'w') as file:
        csv.writer(file).writerows(data)

    # Return a confirmation message
    if command_found:
        print (f"Updated '{command}' to '{new_count}' successfully.")
    else:
        print(f"Command '{command}' not found.")

def archive_files():
    # Examples showing shutil module usage
    shutil.make_archive('artifacts', 'zip', 'files')