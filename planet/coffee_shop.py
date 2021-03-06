class CoffeeShop:
    def __init__(self, price):
        self.sell = 0
        self.price = price
        self.stock = 100
    def get_order(self, quantity):
        if quantity < self.stock:
            order_total = self.price * quantity
            self.stock -= quantity
            self.sell += order_total
            print(f"Thank you. You bought {quantity} coffee. Tolal is {order_total}")
        else:
            print(f"Sorry we have only {self.stock} coffee now.")
            self.restock()
    def restock(self):
        self.stock += 100
        print(f"100 Coffee is restocked, we have {self.stock} coffee now.")
        
StarBucks = CoffeeShop(3.5)
StarBucks.get_order(10)
StarBucks.get_order(100)
StarBucks.get_order(100)
# TimHortons = CoffeeShop(1.5)
# StarBucks.get_order(20)
