class Bank:
    def __init__(self, name, age, pin):
        self.name = name
        self.age = age
        self.__pin = pin
    def get_pin(self):
        return self.__pin

Mark = Bank("Mark", 35, 1234)
print(Mark.name)
print(Mark.age)
# print(Mark.__pin)
print(Mark.get_pin())

