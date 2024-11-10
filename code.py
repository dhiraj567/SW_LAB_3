import os
import time

class PasswordManager:
    def __init__(self):
        self.passwords = []
    
    def is_password_strength_valid(self, password):
        if len(password) < 8:
            return False
    
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        special_characters = "!@#$%_-"

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_characters:
                has_special = True
        return has_upper and has_lower and has_digit and has_special

    def get_password(self):
        if self.passwords:
            return self.passwords[-1]
        return None
    
    def set_password(self, new_password):
        if self.is_password_strength_valid(new_password) and new_password not in self.passwords:
            self.passwords.append(new_password)
            print("Password set successfully!")
        elif not self.is_password_strength_valid(new_password):
            print("Password is not strong enough. Please enter a password with at least 8 characters, including uppercase, lowercase, digit, and special character.")
        else:
            print("Password is the same as your previous password. Please enter a different password.")
    
    def is_correct_password(self, password):
        if self.passwords and password == self.passwords[-1]:
            return True
        return False


if __name__ == "__main__":
    pm_object = PasswordManager()
    status = True
    isUserAuthenticated = False
    def clear_screen():
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Password Manager!")
    
    while status:
        print("1. Set Password")
        print("2. Get Password")
        print("3. Check Password")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_password = input("Enter new password: ")
            pm_object.set_password(new_password)
        elif choice == 2:
            if not isUserAuthenticated:
                print("Please authenticate yourself first.")
            else:
                print(pm_object.get_password())
        elif choice == 3:
            password = input("Enter your password: ")
            if pm_object.is_correct_password(password):
                isUserAuthenticated = True
                print("Password is correct!")
            else:
                print("Password is incorrect! (or) no password set yet.")
        elif choice == 4:
            status = False
        else:
            print("Invalid choice. Please enter a valid choice.")
        
        clear_screen()
