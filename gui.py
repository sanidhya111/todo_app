import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo item", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My TO-DO App", layout=[[label, input_box], [add_button]], font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()