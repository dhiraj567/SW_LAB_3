class PasswordManager:
    def __init__(self):
        self.passwords = []
    
    def get_password(self):
        if self.passwords:
            return self.passwords[-1]
        return None
    
    def set_password(self, new_password):
        if new_password not in self.passwords:
            self.passwords.append(new_password)
            print("Password set successfully!")
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
