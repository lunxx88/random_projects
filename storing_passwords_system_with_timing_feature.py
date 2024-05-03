''' 
Created by: Aisha @lunxx88

this code is for practice only, the idea of it is to see how a timing attack works,
hence I put a fixed time when comparing to the inputting passwords.
please let me know if there is an error or any thoughts.
'''
import json
import hashlib
import time


class ModifidedcredentialManager:

    def __init__(self, filename="ModeCredentials.json"):
        self.filename = filename
        self.save_credentials = self.load_credentials()

    def hash_pass(self, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return hashed

    def store_credential(self, username, password):
        hashed = self.hash_pass(password)
        self.save_credentials[username] = hashed
        with open(self.filename, 'w') as f:
            json.dump(self.save_credentials, f)
        print("Credentials stored successfully")

    def load_credentials(self):
        try:
            with open(self.filename, "r") as file:
                credentials = json.load(file)
            return credentials
        except FileNotFoundError:
            return {}

    def varify_credentials(self, username, password):
        if username in self.save_credentials:
            hased = self.save_credentials[username]
            input_hashed_pass = self.hash_pass(password)

            # Perform fixed-time comparison of the hashed passwords
            if len(hased) != len(input_hashed_pass):
                return False
            time.sleep(0.01)

            result = 0
            for x, y in zip(hased, input_hashed_pass):
                result |= ord(x) ^ ord(y)

            return result == 0
        return False

credential_manager = ModifidedcredentialManager()

# store credentials

option = input("sign in or login?: ").lower()

if option == "sign in":
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    credential_manager.store_credential(username, password)
elif option == "login":

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if credential_manager.varify_credentials(username, password):
        print("Credentials verified successfully")
    else:
        print("Invalid username or password")

else:
    print("Invalid Choice! Please Choose Again!")
