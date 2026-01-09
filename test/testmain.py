import sys
from pathlib import Path

# Add the parent directory to sys.path to allow importing main
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from functions import get_todos, save_todos, get_valid_index

def test_get_todos_file_exists(tmp_path):
    """Test reading from an existing file."""
    # Create a dummy file in a temporary directory
    d = tmp_path / "files"
    d.mkdir()
    p = d / "todos.txt"
    p.write_text("Buy milk\nWalk dog\n")
    print("He he")
    print(f"\nTemp file path: {p}")
    
    todos = get_todos(p)
    assert todos == ["Buy milk\n", "Walk dog\n"]

def test_get_todos_file_not_found(tmp_path):
    """Test reading from a non-existent file returns empty list."""
    p = tmp_path / "non_existent.txt"
    todos = get_todos(p)
    assert todos == []

def test_save_todos(tmp_path):
    """Test writing todos to a file."""
    d = tmp_path / "files"
    d.mkdir()
    p = d / "todos.txt"
    todos = ["Task 1\n", "Task 2\n"]
    
    save_todos(p, todos)
    
    assert p.read_text() == "Task 1\nTask 2\n"

def test_save_todos_creates_directory(tmp_path):
    """Test that save_todos creates the directory if it doesn't exist."""
    p = tmp_path / "subdir" / "todos.txt"
    todos = ["New Task\n"]
    
    save_todos(p, todos)
    
    assert p.exists()
    assert p.read_text() == "New Task\n"

def test_get_valid_index_valid(monkeypatch):
    """Test valid index input."""
    # Mock input to return '1'
    monkeypatch.setattr('builtins.input', lambda _: '1')
    todos = ["a", "b", "c"]
    # User enters 1, function should return 0 (0-based index)
    index = get_valid_index(todos, "prompt")
    assert index == 0

def test_get_valid_index_out_of_bounds(monkeypatch, capsys):
    """Test index out of bounds."""
    # Mock input to return '5' (out of bounds for list of 3)
    monkeypatch.setattr('builtins.input', lambda _: '5')
    todos = ["a", "b", "c"]
    
    index = get_valid_index(todos, "prompt")
    
    assert index is None
    # Optional: Check if the error message was printed
    captured = capsys.readouterr()
    assert "Item number 5 is not present" in captured.out

def test_get_valid_index_invalid_input(monkeypatch, capsys):
    """Test non-integer input."""
    # Mock input to return 'abc'
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    todos = ["a", "b", "c"]
    
    index = get_valid_index(todos, "prompt")
    
    assert index is None
    captured = capsys.readouterr()
    assert "Invalid input12" in captured.out