class Watch:
    def __init__(self, brand, price, year):
        self.brand = brand
        self.price = price
        self.year = year
    def recharge(self):
        return "Charging now"
        
apple_watch = Watch("apple", 300, 2019)
print(apple_watch.price)
print(apple_watch.recharge())
diesel_watch = Watch("diesel", 200, 2018)
print(apple_watch.year)
print(apple_watch.recharge())
