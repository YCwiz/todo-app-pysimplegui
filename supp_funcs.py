"""Module that contains supporting logic and functions.

objects - module that contain task and CRUD objects
"""
from objects import *

def view_tasks() :
    """Renders list of tasks that is stored in database and returns it.
    
    CRUD - object/class to help with the database management
    db - instance of CRUD
    list_of_tasks - stores the tasks in a list
    tasks - stores tasks as tuples from database
    """
    db = CRUD()
    list_of_tasks = []
    tasks = db.read_from_db()
    for name, complete in tasks :
        """Unpacks tuple and store it as list."""
        task = Task(name, complete)
        list_of_tasks.append(task.name)

    return list_of_tasks
