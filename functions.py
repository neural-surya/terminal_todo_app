def get_todos(filepath):
    """Reads todos from the file. Returns an empty list if file not found."""
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