from decimal import Decimal, ROUND_HALF_UP


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self._items = {}
    
    def add(self, product, quantity):
        if product in self._items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity
    
    def get_quantity(self, product):
        return self._items.get(product, 0)
    
    def get_unit_price(self, product):
        return product.price
    
    def subtotal(self):
        return sum(product.price * qty for product, qty in self._items.items())
    
    def tax(self, rate):
        tax_amount = Decimal(str(self.subtotal() * rate / 100))
        return float(tax_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
    
    def total(self):
        return round(self.subtotal(), 2)
