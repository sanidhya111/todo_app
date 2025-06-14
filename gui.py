import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('DarkGrey')

clock = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo item", key="todo")
add_button = sg.Button("Add", size= 10)
# add_button = sg.Button(size=15, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Click to Add", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove", size=10)
# remove_button = sg.Button(size=15, image_source="complete.png", mouseover_colors="LightBlue2", tooltip="Click to Remove", key="Remove")
exit_button = sg.Button("Exit")

layout= [[clock],[label, input_box], [add_button],[list_box, edit_button, remove_button],[exit_button]]

window = sg.Window("My TO-DO App", layout=layout, font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%d-%b-%Y, %H:%M:%S"))
    # print(1,event)
    # print(2,values)
    # print(3,values["todos"])
    # print(4,values["todos"][0])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]+ "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values= todos)
            except IndexError:
                sg.popup("Please select an item to edit.", font=("Helvetica", 20))
        case "Remove":
            try:
                todo_to_remove = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item to remove.", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value= values["todos"][0])
        case sg.WINDOW_CLOSED:
            break

window.close()