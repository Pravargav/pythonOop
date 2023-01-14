import csv


class Item:
    pay_rate = 0.8 
    all = []
    def __init__(self, name: str, price: float, quantity=0):
      
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        self.read_only_name=name
        # name variable
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    # name method
    def read_only_name(self):
        return self.read_only_name



    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
  
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"('{self.name}', {self.price}, {self.quantity})"