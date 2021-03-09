class Athlete:
    def __init__(self, sport):
        self.sport = sport
    def get_sport(self):
        return self.sport
        
a1 = Athlete("football")
print(a1.get_sport())
