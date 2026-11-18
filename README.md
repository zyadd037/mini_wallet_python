# Mini Wallet System

A simple Python-based digital wallet simulation that allows users to manage their wallet balance and perform withdrawal operations with custom exception handling.

This project demonstrates the use of Python classes, object-oriented programming fundamentals, and exception handling to manage financial operations safely.

## Features

- Create a wallet with an initial balance.
- Withdraw money from the wallet.
- Check whether the wallet has sufficient funds before withdrawal.
- Prevent withdrawals that exceed the available balance.
- Display the remaining balance after a successful withdrawal.
- Handle insufficient funds using a custom exception.

## OOP and Python Concepts

- **Classes and Objects:** Creating and using a Wallet object.
- **Constructors (`__init__`):** Initializing the wallet with an initial balance.
- **Instance Attributes:** Managing wallet balance using `self`.
- **Custom Exceptions:** Creating `InsufficientFundsError` to handle insufficient balance situations.
- **Exception Handling:** Using `try` and `except` to handle errors without crashing the program.
- **Conditional Statements:** Validating withdrawal operations before updating the balance.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Exception Handling

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Run the following command:

```bash
python mini_wallet.py
```

## Example

The wallet is initialized with a balance of 5000.

When attempting to withdraw 5500, the program raises a custom `InsufficientFundsError` because the requested amount exceeds the available balance.

## Learning Objectives

The main goal of this project is to practice Python OOP fundamentals and understand how custom exceptions can be used to handle errors in real-world applications.

## Author

Zeyad Ahmed Mohamed
