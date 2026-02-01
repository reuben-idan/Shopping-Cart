import pytest
from shopping_cart import ShoppingCart, Product


def test_add_products_to_cart():
    cart = ShoppingCart()
    dove_soap = Product("Dove Soap", 39.99)
    
    cart.add(dove_soap, 5)
    
    assert cart.get_quantity(dove_soap) == 5
    assert cart.get_unit_price(dove_soap) == 39.99
    assert cart.total() == 199.95


def test_add_additional_products_to_cart():
    cart = ShoppingCart()
    dove_soap = Product("Dove Soap", 39.99)
    
    cart.add(dove_soap, 5)
    cart.add(dove_soap, 3)
    
    assert cart.get_quantity(dove_soap) == 8
    assert cart.get_unit_price(dove_soap) == 39.99
    assert cart.total() == 319.92


def test_calculate_tax_with_multiple_items():
    cart = ShoppingCart()
    dove_soap = Product("Dove Soap", 39.99)
    axe_deo = Product("Axe Deo", 99.99)
    
    cart.add(dove_soap, 2)
    cart.add(axe_deo, 2)
    
    assert cart.get_quantity(dove_soap) == 2
    assert cart.get_unit_price(dove_soap) == 39.99
    assert cart.get_quantity(axe_deo) == 2
    assert cart.get_unit_price(axe_deo) == 99.99
    assert cart.tax(12.5) == 35.00
    assert cart.total() + cart.tax(12.5) == 314.96
