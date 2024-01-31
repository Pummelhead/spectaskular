import time
import datetime

class Task:
    def __init__(self, name, description=None, display_time=None, due_time=None, priority=None):
        self.name = name
        self.description = description
        self.dispalay_time = display_time
        self.due_time = due_time
        self.priority = priority
        self.to_display = True
        self.complete = False

def create_task():
    name = None
    while not name:
        name = input("*Required* Task:")
    description = input("Description: ")
    task = Task(name, description)
    return task

if __name__ == "__main__":
    t1 = create_task()
    print(f"Task: {t1.name}\nDescription: {t1.description}")