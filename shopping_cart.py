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
    
    def total(self):
        return round(sum(product.price * qty for product, qty in self._items.items()), 2)
