from bonus.converters136 import convert
from functions import get_todos, write_todos
# OR
# import functions
import time

time_format = f"Today's date is:%d-%m-%Y, Time: %H:%M:%S"
print(time.strftime(time_format))

while True:
    user_action = input("Type (add/new, show, edit, complete or exit) along with your action:")
    user_action = user_action.strip()
    user_action = user_action.lower()


    if user_action.startswith("add") or user_action.startswith("new"):
        # todo = user_action.split("add ")[1]
        todo = user_action[4:]

        todos = get_todos()
        # OR
        # todos = functions.get_todos()

        todos.append(todo + "\n")

        write_todos(todos)


    elif user_action.startswith("show") :
        todos = get_todos()

        # new_todos = [item.strip("\n") for item in todos]       # List comprehension
        # print(new_todos)

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1}.{item}")

    elif user_action.startswith("edit") :
        try:
            todos = get_todos()

            print(todos)
            # number = int(user_action.split("edit ")[1])
            number = int(user_action[5:])

            str_item = todos[number - 1]
            # item_content_stripped = str_item.strip("\n")
            print(f"This is the item '{str_item.strip("\n")}' that you entered")
            new_todo = input("Enter the item you want to replace it with:")
            todos [number-1] = new_todo + "\n"
            print(f"Updated list: {todos}")

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete") :
        try:
            todos = get_todos()

            # number = int(user_action.split("complete ")[1])
            number = int(user_action[8:])

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            message = f"{todo_to_remove} was removed from the list"
            print(message)

            write_todos(todos)

        except IndexError:
            print("Your number is out of range")
            continue

    elif user_action.startswith("exit") :
        break

    else:
        print("Hey!, you entered a wrong command")

print("Bye!")
print("Good Bye!")


