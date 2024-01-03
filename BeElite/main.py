import tkinter as tk

class BankAccount:
    def __init__(self, account_number, initial_balance, account_holder_name):
        self.__account_number = account_number
        self.__balance = initial_balance
        self.account_holder_name = account_holder_name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account System")
        
        self.bank_account = BankAccount(account_number="12345", initial_balance=1000, account_holder_name="John Doe")

        self.label = tk.Label(root, text="Bank Account System", font=("Arial", 16))
        self.label.pack(pady=10)

        self.balance_label = tk.Label(root, text="Balance: $0.00")
        self.balance_label.pack()

        self.deposit_entry = tk.Entry(root)
        self.deposit_entry.pack()

        # deposit button
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_entry = tk.Entry(root)
        self.withdraw_entry.pack()

        # withdraw button
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.update_balance()

    def deposit(self):
        amount = float(self.deposit_entry.get())
        self.bank_account.deposit(amount)
        self.update_balance()

    def withdraw(self):
        amount = float(self.withdraw_entry.get())
        self.bank_account.withdraw(amount)
        self.update_balance()

    def update_balance(self):
        balance = self.bank_account.get_balance()
        self.balance_label.config(text=f"Balance: ${balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
