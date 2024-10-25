import streamlit as st
import functions

# Retrieve the current list of todos from the 'functions' module
todos = functions.get_todos()

def add_todo():
    """Function to add a new todo item to the list."""
    # Get the new todo item from the session state and add a newline character
    todo = st.session_state["new_todo"] + "\n"
    # Add the new todo item to the list of todos
    todos.append(todo)
    # Write the updated list of todos to the storage (e.g., a file or database)
    functions.write_todos(todos)

# Set the title of the app
st.title("My todo app")
# Display a brief description of the app using HTML for text formatting
st.write("This app helps in increasing your <b>Productivity</b>", unsafe_allow_html=True)

# Loop through the current list of todos and create a checkbox for each item
for index, todo in enumerate(todos):
    # Create a checkbox with the todo item text as the label and use the todo item as the key
    checkbox = st.checkbox(todo, key=todo)
    
    # If the checkbox is checked, remove the corresponding todo item from the list
    if checkbox:
        # Remove the todo item from the list based on its index
        todos.pop(index)
        # Write the updated list of todos to storage
        functions.write_todos(todos)
        # Remove the item from the session state
        del st.session_state[todo]
        # Rerun the app to refresh the interface with updated todos
        st.experimental_rerun()

# Create a text input field for adding a new todo item
st.text_input(
    label='',  # No label displayed above the text input
    placeholder='Add a new todo...',  # Placeholder text inside the input field
    on_change=add_todo,  # Function to be called when the user presses Enter
    key='new_todo'  # Key used to store the new todo item in session state
)
