#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total * (1 - self.discount/100))
            print(f"After the discount, the total comes to ${self.total}.")
            return self.total
        else:
            print("There is no discount to apply.")
            return False

    def void_last_transaction(self):
        if self.items: 
            self.total -= self.last_transaction
            
            for _ in range(int(self.last_transaction / (self.last_transaction/len(self.items[-1:])))):
                self.items.pop()
            self.last_transaction = 0.0
            if not self.items:  
                self.total = 0.0