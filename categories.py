from task import Task

class Category:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.tasks = []

def create_category():
    name = None
    while not name:
        name = input("*Required* Task:")
    description = input("Description: ")
    category = Category(name, description)
    return category