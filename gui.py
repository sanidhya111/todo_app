import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(key="input_text", default_text="")
add_button = sg.Button("Add")

window = sg.Window("My TO-DO App", layout=[[label, input_box], [add_button]], font=("Helvetica", 20))
window.read()
window.close()