# Shopping-Cart
shopping-cart-problem.

## Version
5113b52715be4c01a8f6db83d38b8d75ee924c88

## Requirements
- Python 3.7 or higher
- pip (Python package manager)

## Setup and Running Tests

### Windows
```
build.bat
```

### Unix/Linux/Mac
```
chmod +x build.sh
./build.sh
```

### Manual Setup
```
pip install -r requirements.txt
python -m pytest -v
```

## Project Structure
- `shopping_cart.py` - Main implementation (Product and ShoppingCart classes)
- `test_shopping_cart.py` - Unit tests
- `requirements.txt` - Python dependencies
- `build.bat` / `build.sh` - Automated build scripts

## Step 1 Complete
Implemented shopping cart with ability to add products and calculate total price.

## Step 2 Complete
Added support for adding additional products of the same type to the cart.
