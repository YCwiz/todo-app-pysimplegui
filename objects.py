"""Module to contain task objects and CRUD

sqlite3 - module for database management
Task - instance of an task
CRUD - object to help with CRUD
"""
import sqlite3

class Task:
    """Task object."""

    def __init__(self,name="", complete = False) :
        """
        name - description of the task
        complete - boolean type to indicate if taask is complete or not
                   (will only be used in later update of app)"""
        self.name = name
        self.complete = complete

    def edit_name(self, old_name, new_name, complete = False) :
        """A self initialization method.
        
        new_name - contains new descfiption of task
        old_name -  contains old/original description
        complete - task is complete or not
        """
        self.name = new_name
        self.old_name = old_name
        self.complete = complete

class CRUD:
    """This object will be responsible for database management."""

    def __init__(self):
        """Establish connection or create new database and table.
        
        self.connect - create/connect database
        self.cursor - allows to update/write/delete values of database
        self.connect.commit - makes changes to database take effect
        """
        self.connect = sqlite3.connect("todo.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS todos(
            name TEXT,
            complete BOOLEAN
        )""")
        self.connect.commit()

    def read_from_db(self) :
        """Retrieve tasks from database.
        
        self.cursor.fetchall() - stores retrieved values temporarily
        tasks - variable to store task values
        self.connect.close() - close connection to database
        """
        self.connect
        self.cursor.execute("""SELECT * FROM todos""")
        tasks = self.cursor.fetchall()
        self.connect.close()
        return tasks
    
    def add_to_db(self, task) :
        """Enters tasks to database.
        
        task - task object that needs to be added to database
        """
        self.connect
        self.cursor.execute("""INSERT INTO todos
                            VALUES (?, ?)""", (task.name, task.complete))
        self.connect.commit()
        self.connect.close()
    
    def update_db(self, task) :
        """Method allow for edits to be made to tasks.
        
        task - task object containing old name and new name
        """
        self.connect
        self.cursor.execute("""UPDATE todos
                            SET name = (?)
                            WHERE name = (?)""", (task.name, task.old_name))
        self.connect.commit()
        self.connect.close()

    def remove_from_db(self, task) :
        """Method allow for deletion of a task from database.
        
        task - task object that needs to be removed
        """
        self.connect
        self.cursor.execute("""DELETE 
                            FROM todos
                            WHERE name = (?)""", (task.name,))
        self.connect.commit()
        self.connect.close()
