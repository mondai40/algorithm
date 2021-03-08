class SmartDevice:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def recharge(self):
        return "Charging now"

class Phone(SmartDevice):
    def __init__(self, brand, price, color):
        SmartDevice.__init__(self, brand, price)
        self.color = color

class Watch(SmartDevice):
    def __init__(self, brand, price, year):
        SmartDevice.__init__(self, brand, price)
        self.year = year

iphone = Phone("apple", 900, "black")
print(iphone.brand)
print(iphone.recharge())
apple_watch = Watch("apple", 300, 1987)
print(apple_watch.year)
print(apple_watch.recharge())
