class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def get_name(self):
        return self.name
        
class Athlete:
    def __init__(self, sport):
        self.sport = sport
    def get_sport(self):
        return self.sport
        
class Person(Student, Athlete):
    def __init__(self, id, name, sport):
        Student.__init__(self, id, name)
        Athlete.__init__(self, sport)

Messi = Person(23, "Messi", "soccer")
print(Messi.get_name())
print(Messi.get_sport())
