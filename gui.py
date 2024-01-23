"""Main module for app.

Contains all widgets and most logic for app to be operational.
objects - module that contains task and CRUD classes
supp_funcs - module to contain all support functions and logic
PySimpleGUI - module that allows for creation of GUI
"""
from objects import *
from supp_funcs import *
import PySimpleGUI as psg

"""Widgets for Graphical User Interface."""
label = psg.Text("Type in a to-do",)
input_box = psg.InputText(tooltip="Enter todo", key = "task")
add_button = psg.Button("Add")
list_box = psg.Listbox(values=view_tasks(), key="sel_task", enable_events=True, size=[50, 10])
edit_button = psg.Button("Edit", key="edit")
delete_button = psg.Button("Delete", key="delete")

"""variable containing the layout of the widgets."""
layout = [
        [label],
        [input_box, add_button],
        [list_box, edit_button, delete_button]
]
"""Main window of Graphical User Interface."""
window = psg.Window("My To-Do App", 
                    layout=layout,
                    font = ("Helvetica") )

while True:
    """Loop ensures app does not stop after an action is taken.
    
    window.read() - track all action made on interface
    event - stores action taken last
    key - stores the additional changes/ actions taken
    """
    event, key = window.read()
    
    """Gets the last action taken and matches it for appropriate action."""
    match event :
    
        case "Add" :
            """Logic applies when the add button is pressed."""
            name = key["task"]

            """Ensures that values are entered into input box"""
            if len(name) > 0 :
                task = Task(name)
                db = CRUD()
                db.add_to_db(task)

                """Allows list box to be refreshed after task has been added."""
                window["sel_task"].update(values= view_tasks())

            else :
                continue

        case "edit" :
            """Logic applies when edit button is pressed."""
            task = Task()
            """Ensures that user enter values in input box"""
            try :
                old_name = key["sel_task"][0]

                new_name = key["task"]
                task.edit_name(old_name,new_name )
                db = CRUD()
                db.update_db(task)

                """Allows list box to be refreshed after task has been edited."""
                window["sel_task"].update(values= view_tasks())

            except IndexError:
                continue
        
        case "delete" :
            """Logic applies when delete button is pressed."""
            """Ensures that user did select a task to be deleted."""
            try :
                name = key["sel_task"][0]
                task = Task(name)
                db = CRUD()
                db.remove_from_db(task)

                """Allow the list box to be refreshed after deleting a task."""
                window["sel_task"].update(values= view_tasks())
                
            except IndexError :
                continue

        case "sel_task" :
            """Allow selectedd task to be displayed in input box."""
            window["task"].update(value=key["sel_task"][0])

        case psg.WIN_CLOSED :
            """Breaks the loop when user exits the app."""
            break

window.close()
