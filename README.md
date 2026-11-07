# Supermarket Bill Generator

**Mini Project – Python Programming (3rd Semester)**

A console-based supermarket billing application developed in Python. It allows a customer to select products and quantities, calculates item-wise GST, and prints an itemized receipt.

## Features

- Product catalogue containing product ID, name, unit price, and GST percentage.
- Customer name, product IDs, and quantities as input.
- Item-wise base cost and GST calculation.
- Subtotal, total GST, and final payable amount.
- Formatted console bill using Python f-strings.
- Invalid product IDs are skipped with a warning.
- Checks that the number of product IDs matches the number of quantities.

## Requirements

- Python 3.8 or later
- No external packages required.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python bill_generator.py
   ```

4. Enter the customer name.
5. Enter product IDs as a Python list, for example:

   ```python
   ['P1', 'P3', 'P5']
   ```

6. Enter quantities in the same order, for example:

   ```python
   [2, 1, 1]
   ```

## Product Catalogue

| ID | Product | Price (Rs.) | GST |
|---|---|---:|---:|
| P1 | Basmati Rice (1kg) | 120.00 | 5% |
| P2 | Sunflower Oil (1L) | 150.00 | 5% |
| P3 | Toothpaste (200g) | 95.00 | 12% |
| P4 | Notebook (Pack of 5) | 175.00 | 12% |
| P5 | Bluetooth Earphones | 1499.00 | 18% |
| P6 | Cotton T-Shirt | 599.00 | 18% |
| P7 | Chocolate Box | 249.00 | 18% |
| P8 | Wooden Table Lamp | 899.00 | 18% |

## Example

For product IDs `['P1', 'P3', 'P5']` and quantities `[2, 1, 1]`:

- Subtotal before GST: Rs. 1834.00
- Total GST: Rs. 293.22
- Total payable: Rs. 2127.22

## Python Concepts Used

- Dictionaries and lists
- Functions
- Loops and conditional statements
- `zip()` for iterating over product IDs and quantities
- Numeric types and arithmetic operations
- Input handling and safe literal parsing with `ast.literal_eval()`
- String formatting with f-strings

## Student Details

- **Name:** Harshit More
- **USN:** 25BTRPW046
- **Course:** B.Tech CSE (General)
- **Class & Section:** CSE-Gen (D)
- **Faculty:** Ms. Sujithra G

## License

This project was created as an academic mini project.
