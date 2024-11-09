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
        special_characters = "!@#$%^&*()-_=+[{]}\|;:,<.>/?`~"

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
    pm_object.set_password("password")
    print(pm_object.get_password())
    print(pm_object.is_correct_password("password"))
    print(pm_object.is_correct_password("password1"))
    
    pm_object.set_password("password")
    
    pm_object.set_password("password1")
    
    print(pm_object.get_password())
    print(pm_object.is_correct_password("password"))
    print(pm_object.is_correct_password("password1"))
