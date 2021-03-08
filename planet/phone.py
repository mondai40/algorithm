class Phone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    def recharge(self):
        return "Chargin now."
        
iphone = Phone("apple", 900, "black")
print(iphone.brand)
print(iphone.recharge())
xeperia = Phone("sony", 900, "silve")
print(iphone.color)
print(iphone.recharge())
