import streamlit as st
import functions
import warnings
warnings.filterwarnings("ignore", message="pkg_resources is deprecated.*")


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear input


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")



for i, todo in enumerate(todos):
    if st.checkbox(todo, key=f"checkbox_{i}"):
        todos.pop(i)
        functions.write_todos(todos)
        st.rerun()

st.text_input(label="", placeholder="Enter a todo item",
              on_change=add_todo, key="new_todo")

st.session_state