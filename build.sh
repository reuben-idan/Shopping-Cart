#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running tests..."
python -m pytest -v

echo "Build complete!"
