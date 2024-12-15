import tkinter as tk
from tkinter import messagebox

# Hard-coded exchange rates (example values)
EXCHANGE_RATES = {
    "USD": {"EUR": 0.85, "INR": 74.5},
    "EUR": {"USD": 1.18, "INR": 88.0},
    "INR": {"USD": 0.013, "EUR": 0.011},
}

def convert_currency():
    """
    Handles the conversion process triggered by the GUI button.
    """
    base_currency = base_currency_entry.get().upper()
    target_currency = target_currency_entry.get().upper()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the amount.")
        return

    if base_currency in EXCHANGE_RATES and target_currency in EXCHANGE_RATES[base_currency]:
        exchange_rate = EXCHANGE_RATES[base_currency][target_currency]
        converted_amount = amount * exchange_rate
        result_label.config(
            text=f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}"
        )
    else:
        messagebox.showerror(
            "Error",
            f"Exchange rate from {base_currency} to {target_currency} not available.",
        )
        result_label.config(text="Conversion failed. Check inputs.")

# Create the GUI window
root = tk.Tk()
root.title("Currency Converter")

# Create and place the widgets
tk.Label(root, text="Base Currency:").grid(row=0, column=0, padx=10, pady=5)
base_currency_entry = tk.Entry(root)
base_currency_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Target Currency:").grid(row=1, column=0, padx=10, pady=5)
target_currency_entry = tk.Entry(root)
target_currency_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Amount:").grid(row=2, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
