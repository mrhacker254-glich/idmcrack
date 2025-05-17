import tkinter as tk
from tkinter import messagebox
import webbrowser
import winreg

# ---------- CONFIGURABLE SECTION ----------
BINANCE_ID = "1059153701"  # 🔁  <— Replace with your actual Binance Pay ID
BUY_ME_A_COFFEE_URL = "https://www.buymeacoffee.com/josetek"  # 🔁  <— Replace with your link
# ------------------------------------------

def open_buymeacoffee():
    """Open the Buy‑Me‑a‑Coffee page in the default browser."""
    webbrowser.open_new(BUY_ME_A_COFFEE_URL)


def delete_registry_key():
    """Attempt to delete the hard‑coded registry key."""
    try:
        hive = winreg.HKEY_USERS
        key_path = (r"S-1-5-21-1874298818-1245826727-3372292461-1002_Classes"
                    r"\\WOW6432Node\\CLSID\\{07999AC3-058B-40BF-984F-69EB1E554CA7}")
        winreg.DeleteKey(hive, key_path)
        messagebox.showinfo("Success", f"SUCCESSFULLY CRACKED ")
    except FileNotFoundError:
        messagebox.showwarning("CRACKED", "ALREADY ACTIVATE ALL THENKS TO JOSETEK.")
    except PermissionError:
        messagebox.showerror("Permission Denied", "Administrator privileges are required to delete this registry key.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: TRY AGAIN")


def on_delete_click():
    if messagebox.askyesno("Confirm", "CRACK IDM FOR FREE"):
        delete_registry_key()


# -------------------- GUI --------------------
root = tk.Tk()
root.title("IDM cracker tool")
root.geometry("420x220")
root.resizable(False, False)

# Heading
label = tk.Label(root, text="crack IDM", font=("Arial", 12))
label.pack(pady=10)

# Delete button
delete_button = tk.Button(root, text="CRACK IDM", command=on_delete_click, width=20)
delete_button.pack(pady=5)

# Separator
separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=20, pady=10)

# Thanks / donation section
thanks_lbl = tk.Label(root, text="Thanks for using this tool!", font=("Arial", 10))
thanks_lbl.pack()

binance_lbl = tk.Label(root, text=f"Donate via Binance Pay ID: {BINANCE_ID}", fg="blue", cursor="hand2")
# Copy ID to clipboard on click for convenience
binance_lbl.bind("<Button-1>", lambda e: (root.clipboard_clear(), root.clipboard_append(BINANCE_ID), messagebox.showinfo("Copied", "Binance ID copied to clipboard.")))
binance_lbl.pack(pady=2)

coffee_btn = tk.Button(root, text="☕ Buy me a coffee", command=open_buymeacoffee)
coffee_btn.pack(pady=2)

root.mainloop()
