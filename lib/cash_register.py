class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total
        self.last_transaction = transaction_total
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0