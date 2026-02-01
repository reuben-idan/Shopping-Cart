import pytest
from shopping_cart import ShoppingCart, Product


def test_add_products_to_cart():
    cart = ShoppingCart()
    dove_soap = Product("Dove Soap", 39.99)
    
    cart.add(dove_soap, 5)
    
    assert cart.get_quantity(dove_soap) == 5
    assert cart.get_unit_price(dove_soap) == 39.99
    assert cart.total() == 199.95
