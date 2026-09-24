"""
Banking System - Mini Project
A menu-driven Python application that simulates basic banking operations.

Concepts used: variables & data types, conditionals, loops, functions,
lists & dictionaries, string operations, modules (random, datetime).
"""

import random
from datetime import datetime

# All accounts are stored in a dictionary: {account_number: account_dict}
accounts = {}


# ---------------------------------------------------------------- helpers
def now():
    """Return the current date and time as a readable string."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def generate_account_number():
    """Generate a unique 10-digit account number."""
    while True:
        acc_no = str(random.randint(1000000000, 9999999999))
        if acc_no not in accounts:
            return acc_no


def add_transaction(account, kind, amount, details=""):
    """Record a transaction in the account's history list."""
    account["history"].append({
        "time": now(),
        "type": kind,
        "amount": amount,
        "balance": account["balance"],
        "details": details,
    })


def read_amount(prompt):
    """Ask for a positive number. Returns None if the input is invalid."""
    text = input(prompt).strip()
    try:
        amount = float(text)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return None
    if amount <= 0:
        print("Amount must be greater than zero.")
        return None
    return round(amount, 2)


def read_pin(prompt):
    """Ask for a 4-digit PIN. Returns None if the input is invalid."""
    pin = input(prompt).strip()
    if len(pin) == 4 and pin.isdigit():
        return pin
    print("PIN must be exactly 4 digits.")
    return None


# ------------------------------------------------------- main menu actions
def create_account():
    print("\n--- CREATE ACCOUNT ---")
    name = input("Enter your name: ").strip().title()
    if name == "" or not name.replace(" ", "").isalpha():
        print("Invalid name. Use letters only.")
        return

    phone = input("Enter phone number (10 digits): ").strip()
    if len(phone) != 10 or not phone.isdigit():
        print("Invalid phone number.")
        return

    pin = read_pin("Create a 4-digit PIN: ")
    if pin is None:
        return
    if input("Confirm PIN: ").strip() != pin:
        print("PINs do not match. Account not created.")
        return

    acc_no = generate_account_number()
    accounts[acc_no] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "history": [],
    }
    print("\nAccount created successfully!")
    print(f"Account Holder : {name}")
    print(f"Account Number : {acc_no}  (save this for login)")


def login():
    print("\n--- LOGIN ---")
    acc_no = input("Enter account number: ").strip()
    pin = input("Enter PIN: ").strip()

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(f"\nWelcome, {accounts[acc_no]['name']}!")
        return acc_no
    print("Invalid account number or PIN.")
    return None


# ------------------------------------------------------ account menu actions
def check_balance(account):
    print(f"\nCurrent balance: Rs. {account['balance']:.2f}")


def deposit(account):
    amount = read_amount("Enter amount to deposit: ")
    if amount is None:
        return
    account["balance"] += amount
    add_transaction(account, "Deposit", amount)
    print(f"Rs. {amount:.2f} deposited. New balance: Rs. {account['balance']:.2f}")


def withdraw(account):
    amount = read_amount("Enter amount to withdraw: ")
    if amount is None:
        return
    if amount > account["balance"]:
        print("Insufficient balance.")
        return
    account["balance"] -= amount
    add_transaction(account, "Withdrawal", amount)
    print(f"Rs. {amount:.2f} withdrawn. New balance: Rs. {account['balance']:.2f}")


def transfer(acc_no, account):
    receiver_no = input("Enter receiver account number: ").strip()
    if receiver_no not in accounts:
        print("Receiver account not found.")
        return
    if receiver_no == acc_no:
        print("You cannot transfer money to your own account.")
        return

    receiver = accounts[receiver_no]
    amount = read_amount(f"Enter amount to transfer to {receiver['name']}: ")
    if amount is None:
        return
    if amount > account["balance"]:
        print("Insufficient balance.")
        return

    account["balance"] -= amount
    receiver["balance"] += amount
    add_transaction(account, "Transfer Sent", amount, f"To {receiver_no}")
    add_transaction(receiver, "Transfer Received", amount, f"From {acc_no}")
    print(f"Rs. {amount:.2f} transferred to {receiver['name']}.")
    print(f"New balance: Rs. {account['balance']:.2f}")


def show_history(account):
    print("\n--- TRANSACTION HISTORY ---")
    if not account["history"]:
        print("No transactions yet.")
        return
    print(f"{'Date & Time':<20} {'Type':<18} {'Amount':>10} {'Balance':>11}  Details")
    print("-" * 78)
    for t in account["history"]:
        print(f"{t['time']:<20} {t['type']:<18} {t['amount']:>10.2f} "
              f"{t['balance']:>11.2f}  {t['details']}")


def change_pin(account):
    if input("Enter old PIN: ").strip() != account["pin"]:
        print("Incorrect old PIN.")
        return
    new_pin = read_pin("Enter new 4-digit PIN: ")
    if new_pin is None:
        return
    if input("Confirm new PIN: ").strip() != new_pin:
        print("PINs do not match. PIN not changed.")
        return
    account["pin"] = new_pin
    print("PIN changed successfully.")


def account_menu(acc_no):
    account = accounts[acc_no]
    while True:
        print("\n┌─────────────────────────┐")
        print("│      ACCOUNT MENU       │")
        print("├─────────────────────────┤")
        print("│ 1. Check Balance        │")
        print("│ 2. Deposit              │")
        print("│ 3. Withdraw             │")
        print("│ 4. Transfer             │")
        print("│ 5. Transaction History  │")
        print("│ 6. Change PIN           │")
        print("│ 7. Logout               │")
        print("└─────────────────────────┘")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            check_balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            transfer(acc_no, account)
        elif choice == "5":
            show_history(account)
        elif choice == "6":
            change_pin(account)
        elif choice == "7":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


def main():
    print("=" * 34)
    print("   WELCOME TO PYTHON BANKING SYSTEM")
    print("=" * 34)
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            acc_no = login()
            if acc_no:
                account_menu(acc_no)
        elif choice == "3":
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
