"""
FreshMart Billing Dashboard
Run with: python dashboard.py
Uses only Python's standard library (Tkinter).
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

PRODUCTS = {
    "P1": ("Basmati Rice (1 kg)", 120.00, 5),
    "P2": ("Sunflower Oil (1 L)", 150.00, 5),
    "P3": ("Toothpaste (200 g)", 95.00, 12),
    "P4": ("Notebook (Pack of 5)", 175.00, 12),
    "P5": ("Bluetooth Earphones", 1499.00, 18),
    "P6": ("Cotton T-Shirt", 599.00, 18),
    "P7": ("Chocolate Box", 249.00, 18),
    "P8": ("Wooden Table Lamp", 899.00, 18),
}


class BillingDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("FreshMart | Billing Dashboard")
        self.root.geometry("1120x740")
        self.root.minsize(980, 650)
        self.root.configure(bg="#eef2f7")
        self.cart = {}
        self.customer_var = tk.StringVar()
        self.product_var = tk.StringVar()
        self.qty_var = tk.StringVar(value="1")
        self._style()
        self._build()
        self.refresh_cart()

    def _style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Treeview", rowheight=31, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))
        style.configure("TCombobox", padding=6)

    def _build(self):
        header = tk.Frame(self.root, bg="#142b4a", height=82)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="FreshMart", bg="#142b4a", fg="white",
                 font=("Segoe UI", 23, "bold")).pack(side="left", padx=(24, 12), pady=17)
        tk.Label(header, text="BILLING DASHBOARD", bg="#142b4a", fg="#bcd1ed",
                 font=("Segoe UI", 11, "bold")).pack(side="left", pady=25)
        tk.Label(header, text=datetime.now().strftime("%d %b %Y"),
                 bg="#142b4a", fg="white", font=("Segoe UI", 10)).pack(side="right", padx=24)

        body = tk.Frame(self.root, bg="#eef2f7")
        body.pack(fill="both", expand=True, padx=20, pady=16)

        cards = tk.Frame(body, bg="#eef2f7")
        cards.pack(fill="x", pady=(0, 14))
        self.stat_items = self._stat_card(cards, "ITEMS IN CART", "0", "#2563eb")
        self.stat_subtotal = self._stat_card(cards, "SUBTOTAL", "₹0.00", "#0f766e")
        self.stat_gst = self._stat_card(cards, "GST", "₹0.00", "#d97706")
        self.stat_total = self._stat_card(cards, "TOTAL PAYABLE", "₹0.00", "#7c3aed")

        columns = tk.Frame(body, bg="#eef2f7")
        columns.pack(fill="both", expand=True)
        left = tk.Frame(columns, bg="white", width=350,
                        highlightbackground="#dbe3ed", highlightthickness=1)
        left.pack(side="left", fill="y", padx=(0, 13))
        left.pack_propagate(False)
        right = tk.Frame(columns, bg="white",
                         highlightbackground="#dbe3ed", highlightthickness=1)
        right.pack(side="left", fill="both", expand=True)

        tk.Label(left, text="Add products", bg="white", fg="#142b4a",
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=17, pady=(17, 9))
        tk.Label(left, text="Customer name", bg="white", fg="#526174",
                 font=("Segoe UI", 9)).pack(anchor="w", padx=17)
        ttk.Entry(left, textvariable=self.customer_var).pack(
            fill="x", padx=17, pady=(4, 12), ipady=5)

        tk.Label(left, text="Product", bg="white", fg="#526174",
                 font=("Segoe UI", 9)).pack(anchor="w", padx=17)
        choices = [f"{pid} - {name} | ₹{price:.2f} | GST {rate}%"
                   for pid, (name, price, rate) in PRODUCTS.items()]
        self.product_combo = ttk.Combobox(
            left, state="readonly", textvariable=self.product_var, values=choices)
        self.product_combo.pack(fill="x", padx=17, pady=(4, 12))
        self.product_combo.current(0)

        tk.Label(left, text="Quantity", bg="white", fg="#526174",
                 font=("Segoe UI", 9)).pack(anchor="w", padx=17)
        ttk.Entry(left, textvariable=self.qty_var).pack(
            fill="x", padx=17, pady=(4, 12), ipady=5)

        tk.Button(left, text="+  Add to cart", command=self.add_to_cart,
                  bg="#2563eb", fg="white", activebackground="#1d4ed8",
                  activeforeground="white", relief="flat",
                  font=("Segoe UI", 10, "bold"), cursor="hand2", pady=10
                  ).pack(fill="x", padx=17, pady=(2, 16))

        tk.Label(left, text="Product catalogue", bg="white", fg="#142b4a",
                 font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=17, pady=(0, 7))
        catalogue = tk.Text(left, height=12, bg="#f7f9fc", fg="#334155",
                            font=("Consolas", 9), relief="flat", wrap="word")
        catalogue.pack(fill="both", expand=True, padx=17, pady=(0, 17))
        for pid, (name, price, rate) in PRODUCTS.items():
            catalogue.insert("end", f"{pid}  {name}\n     ₹{price:.2f}  |  GST {rate}%\n\n")
        catalogue.configure(state="disabled")

        tk.Label(right, text="Shopping cart", bg="white", fg="#142b4a",
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=17, pady=(17, 9))
        table_frame = tk.Frame(right, bg="white")
        table_frame.pack(fill="both", expand=True, padx=17)
        cols = ("product", "qty", "price", "gst", "total")
        self.tree = ttk.Treeview(table_frame, columns=cols, show="headings")
        headings = {"product": "PRODUCT", "qty": "QTY", "price": "UNIT PRICE",
                    "gst": "GST", "total": "LINE TOTAL"}
        for col, label in headings.items():
            self.tree.heading(col, text=label)
        self.tree.column("product", width=220, anchor="w")
        self.tree.column("qty", width=55, anchor="center")
        self.tree.column("price", width=95, anchor="e")
        self.tree.column("gst", width=105, anchor="e")
        self.tree.column("total", width=115, anchor="e")
        scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        actions = tk.Frame(right, bg="white")
        actions.pack(fill="x", padx=17, pady=13)
        tk.Button(actions, text="Remove selected", command=self.remove_selected,
                  bg="#e2e8f0", fg="#334155", relief="flat",
                  font=("Segoe UI", 9, "bold"), padx=10, pady=8
                  ).pack(side="left")
        tk.Button(actions, text="Clear cart", command=self.clear_cart,
                  bg="#fee2e2", fg="#991b1b", relief="flat",
                  font=("Segoe UI", 9, "bold"), padx=10, pady=8
                  ).pack(side="left", padx=7)
        tk.Button(actions, text="Generate / Save receipt", command=self.generate_receipt,
                  bg="#0f766e", fg="white", relief="flat",
                  font=("Segoe UI", 9, "bold"), padx=10, pady=8
                  ).pack(side="right")

        tk.Label(self.root, text="Python Tkinter  •  GST billing  •  No third-party packages",
                 bg="#eef2f7", fg="#64748b", font=("Segoe UI", 9)).pack(pady=(0, 7))

    def _stat_card(self, parent, title, value, accent):
        card = tk.Frame(parent, bg="white", highlightbackground="#dbe3ed",
                        highlightthickness=1)
        card.pack(side="left", fill="x", expand=True, padx=5)
        tk.Frame(card, bg=accent, height=4).pack(fill="x")
        tk.Label(card, text=title, bg="white", fg="#64748b",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=11, pady=(8, 2))
        label = tk.Label(card, text=value, bg="white", fg="#142b4a",
                         font=("Segoe UI", 16, "bold"))
        label.pack(anchor="w", padx=11, pady=(0, 9))
        return label

    def _selected_pid(self):
        return self.product_var.get().split(" - ", 1)[0].strip()

    def add_to_cart(self):
        pid = self._selected_pid()
        try:
            qty = int(self.qty_var.get())
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid quantity", "Enter a positive whole number.")
            return
        if pid not in PRODUCTS:
            messagebox.showerror("Product", "Select a valid product.")
            return
        self.cart[pid] = self.cart.get(pid, 0) + qty
        self.qty_var.set("1")
        self.refresh_cart()

    def _totals(self):
        subtotal = gst = total = 0.0
        count = 0
        for pid, qty in self.cart.items():
            _, price, rate = PRODUCTS[pid]
            base = price * qty
            tax = base * rate / 100
            subtotal += base
            gst += tax
            total += base + tax
            count += qty
        return count, subtotal, gst, total

    def refresh_cart(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for pid, qty in self.cart.items():
            name, price, rate = PRODUCTS[pid]
            base = price * qty
            tax = base * rate / 100
            line_total = base + tax
            self.tree.insert("", "end", iid=pid,
                             values=(name, qty, f"₹{price:.2f}",
                                     f"{rate}% (₹{tax:.2f})", f"₹{line_total:.2f}"))
        count, subtotal, gst, total = self._totals()
        self.stat_items.config(text=str(count))
        self.stat_subtotal.config(text=f"₹{subtotal:.2f}")
        self.stat_gst.config(text=f"₹{gst:.2f}")
        self.stat_total.config(text=f"₹{total:.2f}")

    def remove_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Remove item", "Select a cart item first.")
            return
        for pid in selected:
            self.cart.pop(pid, None)
        self.refresh_cart()

    def clear_cart(self):
        if self.cart and messagebox.askyesno("Clear cart", "Remove all cart items?"):
            self.cart.clear()
            self.refresh_cart()

    def _receipt(self):
        customer = self.customer_var.get().strip() or "Guest"
        _, subtotal, gst, total = self._totals()
        lines = [
            "=" * 68, "FRESHMART - CUSTOMER RECEIPT".center(68), "=" * 68,
            f"Customer: {customer}",
            f"Date: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}",
            "-" * 68,
            f"{'Product':<27}{'Qty':>5}{'Price':>11}{'GST':>8}{'Total':>14}",
            "-" * 68,
        ]
        for pid, qty in self.cart.items():
            name, price, rate = PRODUCTS[pid]
            base = price * qty
            tax = base * rate / 100
            lines.append(f"{name[:27]:<27}{qty:>5}{price:>11.2f}{rate:>7}%{base + tax:>14.2f}")
        lines += [
            "-" * 68, f"{'Subtotal:':>50} ₹{subtotal:>12.2f}",
            f"{'Total GST:':>50} ₹{gst:>12.2f}",
            f"{'TOTAL PAYABLE:':>50} ₹{total:>12.2f}",
            "=" * 68, "Thank you for shopping!".center(68), "=" * 68,
        ]
        return "\n".join(lines)

    def generate_receipt(self):
        if not self.cart:
            messagebox.showwarning("Empty cart", "Add products before generating a receipt.")
            return
        receipt = self._receipt()
        path = filedialog.asksaveasfilename(
            title="Save receipt", defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            initialfile=f"Receipt_{datetime.now():%Y%m%d_%H%M%S}.txt")
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(receipt)
            messagebox.showinfo("Receipt saved", f"Receipt saved successfully:\n{path}")
            preview = tk.Toplevel(self.root)
            preview.title("Receipt Preview")
            preview.geometry("640x560")
            text = tk.Text(preview, font=("Consolas", 10), wrap="none")
            text.pack(fill="both", expand=True, padx=10, pady=10)
            text.insert("1.0", receipt)
            text.configure(state="disabled")
        except OSError as exc:
            messagebox.showerror("Save error", f"Could not save receipt:\n{exc}")


if __name__ == "__main__":
    root = tk.Tk()
    BillingDashboard(root)
    root.mainloop()
