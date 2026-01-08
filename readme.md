# Terminal Todo App

A simple, lightweight command-line Todo application built in Python that allows you to manage your daily tasks directly from the terminal.

## Features

- **Add**: Add a new todo item to your list.
- **Show**: Display all current todo items with their status (pending or completed).
- **Edit**: Modify the text of an existing todo item.
- **Complete**: Mark an existing todo item as done.
- **Exit**: Save changes and quit the application gracefully.

All todo items are **persisted** to a file, so your tasks remain saved between sessions.

## Data Persistence

Todo items are automatically saved to a TXT file located at:

```
files/todos.txt
```

The `files` directory is created automatically if it doesn't exist. Do not delete or manually edit this file while the app is running to avoid data corruption.

## Requirements

- Python 3.10 or higher

## Installation & Setup

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3.10+ installed. You can check your version with:
   ```bash
   python3 --version
   ```

No additional packages are required — this app uses only the Python standard library.

## How to Run

Navigate to the project root directory and run:

```bash
python3 main.py
```

You will be presented with a menu:

```
Todo App Menu:
1. Add a new todo
2. Show all todos
3. Edit a todo
4. Complete a todo
5. Exit

Choose an option (1-5):
```

### Usage Examples

- **Adding a todo**: Choose option 1 and enter your task when prompted.
- **Viewing todos**: Choose option 2 to see a numbered list with status indicators.
- **Editing a todo**: Choose option 3, enter the item number, and provide the new text.
- **Completing a todo**: Choose option 4 and enter the item number to mark it as done.
- **Exiting**: Choose option 5 to save and quit.

## Project Structure

```
.
├── main.py          # Entry point and main application logic
├── files/
│   └── todos.txt    # Auto-generated file storing your todos
└── README.md        # This file
```

## Notes

- Item numbers are 1-based (as shown in the list).
- Invalid inputs are handled gracefully with clear error messages.
- Completed tasks are marked with `[✓]` when displayed.
- Pending tasks are marked with `[ ]`.

Enjoy staying organized from the comfort of your terminal! 🚀