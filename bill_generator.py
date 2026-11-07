# ==========================================
#          CUSTOMER BILL GENERATOR
# ==========================================

# Product catalogue: product ID -> (name, unit price, GST percentage)
product_details = {
    "P1": ("Basmati Rice (1kg)", 120.0, 5),
    "P2": ("Sunflower Oil (1L)", 150.0, 5),
    "P3": ("Toothpaste (200g)", 95.0, 12),
    "P4": ("Notebook (Pack of 5)", 175.0, 12),
    "P5": ("Bluetooth Earphones", 1499.0, 18),
    "P6": ("Cotton T-Shirt", 599.0, 18),
    "P7": ("Chocolate Box", 249.0, 18),
    "P8": ("Wooden Table Lamp", 899.0, 18)
}

# Numeric accumulators and bill line items
counter = 0
subtotal = 0.0
total_gst = 0.0
total_amount = 0.0
line_items = []


def show_menu():
    """Display the available products and their prices."""
    print("\n" + "=" * 55)
    print(f"{'PRODUCT MENU':^55}")
    print("=" * 55)
    print(f"{'ID':<5}{'Product':<25}{'Price (Rs.)':<12}{'GST %'}")
    print("-" * 55)

    for pid, info in product_details.items():
        title, price, gst = info
        print(f"{pid:<5}{title:<25}{price:<12.2f}{gst}")

    print("=" * 55)


def get_customer_and_selection():
    """Collect customer name, product IDs, and quantities."""
    import ast

    customer_name = input("\nEnter customer name: ")
    show_menu()

    print("\nEnter the Product IDs you want to buy as a Python list.")
    print("Example: ['P1', 'P3', 'P5']")
    selected_ids = ast.literal_eval(input("Product IDs: "))

    print("\nEnter the corresponding quantities as a Python list.")
    print("Example: [2, 1, 1]")
    quantities = ast.literal_eval(input("Quantities: "))

    return customer_name, selected_ids, quantities


def calculate_bill(selected_ids, quantities):
    """Calculate item totals, GST, subtotal, and payable amount."""
    global counter, subtotal, total_gst, total_amount

    for pid, qty in zip(selected_ids, quantities):
        if pid not in product_details:
            print(f"Warning: Product ID '{pid}' not found. Skipping.")
            continue

        title, unit_price, gst_percent = product_details[pid]

        counter += 1
        base_cost = unit_price * qty
        gst_amount = (base_cost * gst_percent) / 100
        line_total = base_cost + gst_amount

        subtotal += base_cost
        total_gst += gst_amount

        line_items.append({
            "sno": counter,
            "title": title,
            "qty": qty,
            "unit_price": unit_price,
            "gst_percent": gst_percent,
            "gst_amount": gst_amount,
            "line_total": line_total
        })

    total_amount = subtotal + total_gst


def print_bill(customer_name):
    """Print the formatted customer receipt."""
    print("\n" + "=" * 60)
    print(f"{'CUSTOMER BILL / RECEIPT':^60}")
    print("=" * 60)
    print(f"Customer Name : {customer_name}")
    print(f"Total Items   : {counter}")
    print("-" * 60)

    print(
        f"{'S.No':<5}{'Product':<22}"
        f"{'Qty':<5}{'Price':<10}{'GST':<8}{'Amount':<10}"
    )
    print("-" * 60)

    for item in line_items:
        print(
            f"{item['sno']:<5}"
            f"{item['title']:<22}"
            f"{item['qty']:<5}"
            f"{item['unit_price']:<10.2f}"
            f"{item['gst_amount']:<8.2f}"
            f"{item['line_total']:<10.2f}"
        )

    print("-" * 60)
    print(f"{'Subtotal (before GST)':<45}Rs. {subtotal:>10.2f}")
    print(f"{'Total GST':<45}Rs. {total_gst:>10.2f}")
    print(f"{'TOTAL AMOUNT PAYABLE':<45}Rs. {total_amount:>10.2f}")
    print("=" * 60)
    print(f"{'Thank you for shopping with us!':^60}")
    print("=" * 60)


def main():
    """Run the supermarket bill generator."""
    print("Welcome to the Python Bill Generator!")

    customer_name, selected_ids, quantities = get_customer_and_selection()

    if len(selected_ids) != len(quantities):
        print("\nError: Number of Product IDs and Quantities must match.")
        return

    calculate_bill(selected_ids, quantities)

    if counter == 0:
        print("\nNo valid products were selected. Bill not generated.")
        return

    print_bill(customer_name)


if __name__ == "__main__":
    main()
