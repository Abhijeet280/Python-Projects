"""Bank Management system"""

import random
import json

print("Press 1 to Create a New Account : ")
print("Press 2 to Fetch Details : ")
print("Press 3 to Deposit Money : ")
print("Press 4 to Withdraw Money : ")
print("Press 5 to Update Account Information : ")
print("Press 6 Delete Account : ")

check = int(input("Enter your choice: "))


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

    def create_account(self):
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "address": input("Enter your address: "),
            "phone_number": input("Enter your phone number: "),
            "account_number": random.randint(1000000000, 9999999999),
            "pin": int(input("Enter your 4-digit PIN: ")),
            "balance": 0.0,
        }

        if info["age"] < 18:
            print("You are not eligible to open an account.")
        else:
            print("Account created successfully!")
            print(f"Account Number: {info['account_number']}")
            print(f"Name: {info['name']}")
            print(f"Age: {info['age']}")
            print(f"Address: {info['address']}")
            print(f"Phone Number: {info['phone_number']}")
            print(f"Balance: {info['balance']}")
            print("Please remember your ACCOUNT NUMBER & PIN for future transactions.")

            Bank.data.append(info)
            Bank.save_data()

    def fetch_details(self):
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your 4-digit PIN: "))
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                print("Account Details:")
                print(f"Name: {account['name']}")
                print(f"Age: {account['age']}")
                print(f"Address: {account['address']}")
                print(f"Phone Number: {account['phone_number']}")
                print(f"Balance: {account['balance']}")
                break
            else:
                print("Invalid account number or PIN.")
        else:
            print("Account not found.")

    def deposit_money(self):
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your 4-digit PIN: "))
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                amount = float(input("Enter the amount to deposit: "))
                account["balance"] += amount
                print(f"Deposited {amount}. New balance: {account['balance']}")
                Bank.save_data()
                break
        else:
            print("Invalid account number or PIN.")

    def withdraw_money(self):
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your 4-digit PIN: "))
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                amount = float(input("Enter the amount to withdraw: "))
                if amount > account["balance"]:
                    print("Insufficient balance.")
                else:
                    account["balance"] -= amount
                    print(f"Withdrew {amount}. New balance: {account['balance']}")
                    Bank.save_data()
                break
        else:
            print("Invalid account number or PIN.")

    def update_account(self):
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your 4-digit PIN: "))
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                print("Update your details:")
                account["name"] = input("Enter your name: ")
                account["age"] = int(input("Enter your age: "))
                account["address"] = input("Enter your address: ")
                account["phone_number"] = input("Enter your phone number: ")
                Bank.save_data()
                print("Account updated successfully!")
                break
        else:
            print("Invalid account number or PIN.")

    def delete_account(self):
        account_number = int(input("Enter your account number: "))
        pin = int(input("Enter your 4-digit PIN: "))
        for account in self.data:
            if account["account_number"] == account_number and account["pin"] == pin:
                response = input(
                    "Are you sure you want to delete your account? (Y/N): "
                )
                if response.lower() != "y":
                    print("Account deletion cancelled.")
                else:
                    print("Account deletion confirmed.")

                self.data.remove(account)
                Bank.save_data()
                print("Account deleted successfully!")
                break
        else:
            print("Invalid account number or PIN.")


user = Bank()

if check == 1:
    user.create_account()

if check == 2:
    user.fetch_details()

if check == 3:
    user.deposit_money()

if check == 4:
    user.withdraw_money()

if check == 5:
    user.update_account()

if check == 6:
    user.delete_account()
