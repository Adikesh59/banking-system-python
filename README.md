# Banking System – Python Mini Project

A menu-driven Python application that simulates basic banking operations. Users can create an account, log in securely with an account number and PIN, and perform common banking activities from the terminal.

## Features

- **Create Account** – enter name, phone number and create a 4-digit PIN (a unique 10-digit account number is generated automatically)
- **Login** – using account number and PIN
- **Check Balance** – view the current account balance
- **Deposit** – add money to the account
- **Withdraw** – deduct money after checking the balance
- **Transfer** – send money to another account using the receiver's account number
- **Transaction History** – view deposits, withdrawals and transfers with date and time
- **Change PIN** – enter old PIN, then enter and confirm the new PIN
- **Logout** – end the session and return to the main menu

## Program Flow

```
CREATE ACCOUNT
      ↓
Account Number + PIN
      ↓
    LOGIN
      ↓
┌─────────────────────────┐
│      ACCOUNT MENU       │
├─────────────────────────┤
│ 1. Check Balance        │
│ 2. Deposit              │
│ 3. Withdraw             │
│ 4. Transfer             │
│ 5. Transaction History  │
│ 6. Change PIN           │
│ 7. Logout               │
└─────────────────────────┘
      ↓
   LOGOUT
      ↓
  MAIN MENU
```

## Python Concepts Used

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- String operations
- Modules: `random` (account number generation) and `datetime` (transaction timestamps)

## Requirements

- Python 3.8 or higher (no external libraries needed)

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python banking_system.py
```

On Mac/Linux, use `python3 banking_system.py`.

## Sample Usage

```
--- MAIN MENU ---
1. Create Account
2. Login
3. Exit
Enter your choice (1-3): 1

--- CREATE ACCOUNT ---
Enter your name: Keshav Kumar
Enter phone number (10 digits): 9876543210
Create a 4-digit PIN: 1234
Confirm PIN: 1234

Account created successfully!
Account Number : 4829173650  (save this for login)
```

## Validations

- PIN must be exactly 4 digits
- Phone number must be 10 digits
- Amounts must be numbers greater than zero
- Withdrawals and transfers are blocked if the balance is insufficient
- Transfers to unknown accounts or to your own account are rejected

## Note

Account data is stored in memory only, so all accounts are reset when the program is closed.

## Author

Keshav Kumar – [GitHub: Adikesh59](https://github.com/Adikesh59)
