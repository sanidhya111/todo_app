FILEPATH = "todos.txt"

def get_todos(filepath= FILEPATH):

    """Open and read a text file.
    Also return the list of items."""

    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):

    """ Writes the todo items in the text file. """

    with open(filepath, "w") as file:
        file.writelines(todos_arg)

print(f"I am outside {__name__}")
# How to not execute a section of code
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
