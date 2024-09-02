import json
import os

class bank_acc:
    def __init__(self, username, password, balance: float = 0.0):
        self.username = username
        self.password = password
        self.balance = balance

    def save_to_files(self):
        users = bank_acc.load_users()
        if self.username in users:
            print("Username already exists")
        else:
            users[self.username] = {
                "password": self.password,
                "balance": self.balance
            }
            with open("users.json", "w") as file:
                json.dump(users, file)
            print(f"User {self.username} registered successfully")

    @staticmethod
    def load_users():
        """Load user data from JSON file."""
        if os.path.exists("users.json"):
            with open("users.json", "r") as file:
                return json.load(file)
        return {}

    @staticmethod
    def authenticator(username, password):
        users = bank_acc.load_users()

        if username in users and users[username]["password"] == password:
            print(f"Welcome {username}, you have successfully logged in.")
            return bank_acc(username, password, users[username]["balance"])
        else:
            print("Invalid username or password")
            return None

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        self.save_balance()
        print("\nAmount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            self.save_balance()
            print("\nAmount Withdrawn:", amount)
        else:
            print("\nInsufficient balance")

    def display(self):
        print(f"Your current balance is {self.balance}")

    def save_balance(self):
        users = bank_acc.load_users()
        users[self.username]["balance"] = self.balance
        with open("users.json", "w") as file:
            json.dump(users, file)

def main():
    while True:
        choice = input("Sign up or login? Or type 'exit' to quit: ").lower()
        if choice == 'sign up':
            un = input("\nEnter Username: ")
            ps = input("\nEnter password: ")
            account = bank_acc(un, ps)
            account.save_to_files()

        elif choice == "login":
            un = input("\nEnter Username: ")
            ps = input("\nEnter password: ")
            account = bank_acc.authenticator(un, ps)

            if account:
                while True:
                    action = input("Choose an action: 1 - Check balance, 2 - Deposit, 3 - Withdraw, 4 - Exit: ")

                    if action == '1':
                        account.display()
                    elif action == '2':
                        account.deposit()
                    elif action == '3':
                        account.withdraw()
                    elif action == '4':
                        break
                    else:
                        print("Invalid choice, please choose again.")
        elif choice == 'exit':
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
