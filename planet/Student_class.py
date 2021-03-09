class Student:
    def __init__(self, id, name):
        self.name = name
        self.id = id
    def get_name(self):
        return self.name

s1 = Student(1, "Harry")
print(s1.get_name())
