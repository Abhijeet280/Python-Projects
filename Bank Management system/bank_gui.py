"""Bank Management system"""

import random
import json
import tkinter as tk
from tkinter import messagebox, simpledialog


class Bank:
    database = "data.json"
    data = []

    with open(database, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []

    @classmethod
    def save_data(cls):
        with open(cls.database, "w") as file:
            json.dump(cls.data, file, indent=4)

    def create_account(self, name, age, address, phone_number, pin):
        info = {
            "name": name,
            "age": int(age),
            "address": address,
            "phone_number": phone_number,
            "account_number": random.randint(1000000000, 9999999999),
            "pin": int(pin),
            "balance": 0.0,
        }

        if info["age"] < 18:
            return None, "You are not eligible to open an account."
        else:
            Bank.data.append(info)
            Bank.save_data()
            return info, "Account created successfully!"

    def fetch_details(self, account_number, pin):
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                return account, None
        return None, "Invalid account number or PIN."

    def deposit_money(self, account_number, pin, amount):
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                account["balance"] += amount
                Bank.save_data()
                return account["balance"], None
        return None, "Invalid account number or PIN."

    def withdraw_money(self, account_number, pin, amount):
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                if amount > account["balance"]:
                    return None, "Insufficient balance."
                else:
                    account["balance"] -= amount
                    Bank.save_data()
                    return account["balance"], None
        return None, "Invalid account number or PIN."

    def update_account(self, account_number, pin, name, age, address, phone_number):
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                account["name"] = name
                account["age"] = int(age)
                account["address"] = address
                account["phone_number"] = phone_number
                Bank.save_data()
                return True, None
        return False, "Invalid account number or PIN."

    def delete_account(self, account_number, pin):
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                self.data.remove(account)
                Bank.save_data()
                return True, None
        return False, "Invalid account number or PIN."


# --- GUI Implementation ---


class BankGUI:
    def __init__(self, root):
        self.bank = Bank()
        self.root = root
        self.root.title("Bank Management System")
        self.root.geometry("400x400")
        self.main_menu()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear()
        tk.Label(self.root, text="Bank Management System", font=("Arial", 16)).pack(
            pady=10
        )
        tk.Button(
            self.root,
            text="Create New Account",
            width=25,
            command=self.create_account_form,
        ).pack(pady=5)
        tk.Button(
            self.root, text="Fetch Details", width=25, command=self.fetch_details_form
        ).pack(pady=5)
        tk.Button(
            self.root, text="Deposit Money", width=25, command=self.deposit_money_form
        ).pack(pady=5)
        tk.Button(
            self.root, text="Withdraw Money", width=25, command=self.withdraw_money_form
        ).pack(pady=5)
        tk.Button(
            self.root,
            text="Update Account Information",
            width=25,
            command=self.update_account_form,
        ).pack(pady=5)
        tk.Button(
            self.root, text="Delete Account", width=25, command=self.delete_account_form
        ).pack(pady=5)
        tk.Button(self.root, text="Exit", width=25, command=self.root.quit).pack(
            pady=20
        )

    def create_account_form(self):
        self.clear()
        tk.Label(self.root, text="Create New Account", font=("Arial", 14)).pack(pady=10)
        entries = {}
        for field in ["Name", "Age", "Address", "Phone Number", "4-digit PIN"]:
            tk.Label(self.root, text=field).pack()
            entry = tk.Entry(self.root, show="*" if "PIN" in field else None)
            entry.pack()
            entries[field] = entry

        def submit():
            try:
                name = entries["Name"].get()
                age = int(entries["Age"].get())
                address = entries["Address"].get()
                phone = entries["Phone Number"].get()
                pin = int(entries["4-digit PIN"].get())
                info, msg = self.bank.create_account(name, age, address, phone, pin)
                if info:
                    messagebox.showinfo(
                        "Success",
                        f"{msg}\nAccount Number: {info['account_number']}\nPlease remember your ACCOUNT NUMBER & PIN.",
                    )
                    self.main_menu()
                else:
                    messagebox.showerror("Error", msg)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def fetch_details_form(self):
        self.clear()
        tk.Label(self.root, text="Fetch Account Details", font=("Arial", 14)).pack(
            pady=10
        )
        tk.Label(self.root, text="Account Number").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()
        tk.Label(self.root, text="4-digit PIN").pack()
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()

        def submit():
            try:
                acc = int(acc_entry.get())
                pin = int(pin_entry.get())
                account, err = self.bank.fetch_details(acc, pin)
                if account:
                    details = (
                        f"Name: {account['name']}\n"
                        f"Age: {account['age']}\n"
                        f"Address: {account['address']}\n"
                        f"Phone: {account['phone_number']}\n"
                        f"Balance: {account['balance']}"
                    )
                    messagebox.showinfo("Account Details", details)
                else:
                    messagebox.showerror("Error", err)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def deposit_money_form(self):
        self.clear()
        tk.Label(self.root, text="Deposit Money", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Account Number").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()
        tk.Label(self.root, text="4-digit PIN").pack()
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()
        tk.Label(self.root, text="Amount").pack()
        amt_entry = tk.Entry(self.root)
        amt_entry.pack()

        def submit():
            try:
                acc = int(acc_entry.get())
                pin = int(pin_entry.get())
                amt = float(amt_entry.get())
                new_bal, err = self.bank.deposit_money(acc, pin, amt)
                if err:
                    messagebox.showerror("Error", err)
                else:
                    messagebox.showinfo(
                        "Success", f"Deposited {amt}. New balance: {new_bal}"
                    )
                    self.main_menu()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def withdraw_money_form(self):
        self.clear()
        tk.Label(self.root, text="Withdraw Money", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Account Number").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()
        tk.Label(self.root, text="4-digit PIN").pack()
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()
        tk.Label(self.root, text="Amount").pack()
        amt_entry = tk.Entry(self.root)
        amt_entry.pack()

        def submit():
            try:
                acc = int(acc_entry.get())
                pin = int(pin_entry.get())
                amt = float(amt_entry.get())
                new_bal, err = self.bank.withdraw_money(acc, pin, amt)
                if err:
                    messagebox.showerror("Error", err)
                else:
                    messagebox.showinfo(
                        "Success", f"Withdrew {amt}. New balance: {new_bal}"
                    )
                    self.main_menu()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def update_account_form(self):
        self.clear()
        tk.Label(self.root, text="Update Account Information", font=("Arial", 14)).pack(
            pady=10
        )
        tk.Label(self.root, text="Account Number").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()
        tk.Label(self.root, text="4-digit PIN").pack()
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()
        tk.Label(self.root, text="New Name").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        tk.Label(self.root, text="New Age").pack()
        age_entry = tk.Entry(self.root)
        age_entry.pack()
        tk.Label(self.root, text="New Address").pack()
        addr_entry = tk.Entry(self.root)
        addr_entry.pack()
        tk.Label(self.root, text="New Phone Number").pack()
        phone_entry = tk.Entry(self.root)
        phone_entry.pack()

        def submit():
            try:
                acc = int(acc_entry.get())
                pin = int(pin_entry.get())
                name = name_entry.get()
                age = int(age_entry.get())
                addr = addr_entry.get()
                phone = phone_entry.get()
                success, err = self.bank.update_account(
                    acc, pin, name, age, addr, phone
                )
                if success:
                    messagebox.showinfo("Success", "Account updated successfully!")
                    self.main_menu()
                else:
                    messagebox.showerror("Error", err)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def delete_account_form(self):
        self.clear()
        tk.Label(self.root, text="Delete Account", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Account Number").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()
        tk.Label(self.root, text="4-digit PIN").pack()
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()

        def submit():
            try:
                acc = int(acc_entry.get())
                pin = int(pin_entry.get())
                if messagebox.askyesno(
                    "Confirm", "Are you sure you want to delete your account?"
                ):
                    success, err = self.bank.delete_account(acc, pin)
                    if success:
                        messagebox.showinfo("Success", "Account deleted successfully!")
                        self.main_menu()
                    else:
                        messagebox.showerror("Error", err)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.root, text="Delete", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = BankGUI(root)
    root.mainloop()
