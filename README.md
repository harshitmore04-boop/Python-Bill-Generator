# Supermarket Bill Generator

**Mini Project – Python Programming (3rd Semester)**

A Python supermarket billing project with both a console version and a graphical billing dashboard.

## Versions

- **Console application:** `bill_generator.py`
- **Graphical dashboard:** `dashboard.py` (Tkinter)

## Dashboard Features

- Select products from a drop-down list and enter quantities.
- Add products to a shopping cart; repeated selections combine quantities.
- Live dashboard cards for item count, subtotal, GST, and total payable.
- Remove selected items or clear the cart.
- Generate a receipt preview and save the receipt as a text file.
- Validates quantities and handles empty-cart actions.

## Requirements

- Python 3.8 or later
- Tkinter (included with most standard Windows Python installations)
- No third-party packages required

## Run the Dashboard in VS Code

1. Download or clone this repository.
2. Open the repository folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Run:

   ```powershell
   python dashboard.py
   ```

   On Windows, you can also run:

   ```powershell
   py dashboard.py
   ```

5. The FreshMart Billing Dashboard window will open.

You can also double-click `RUN_DASHBOARD.bat` on Windows.

## Run the Console Version

```powershell
python bill_generator.py
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

## GST Calculation

- GST amount = (Unit price × Quantity × GST rate) / 100
- Line total = (Unit price × Quantity) + GST amount

## Python Concepts Used

Dictionaries, functions, loops, conditionals, input validation, arithmetic operations, Tkinter widgets, event-driven programming, and string formatting.

## Student Details

- **Name:** Harshit More
- **USN:** 25BTRPW046
- **Course:** B.Tech CSE (General)
- **Class & Section:** CSE-Gen (D)
- **Faculty:** Ms. Sujithra G

This project was created as an academic mini project.
