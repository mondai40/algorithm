# make Data class iterator
# the iterator return numbers from 10 to limit number
class Data:
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        self.value = 10
        return self
    def __next__(self):
        item = self.value
        if item > self.limit:
            raise StopIteration
        else:
            self.value += 1
            return item
    
for i in Data(15):
    print(i)
