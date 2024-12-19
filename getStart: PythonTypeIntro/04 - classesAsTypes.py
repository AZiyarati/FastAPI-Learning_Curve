# From Python 3.8-
# In this example below, you can use class as type for function or variable.
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name
