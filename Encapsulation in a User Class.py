class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
        else:
            raise ValueError("Password must be at least 8 characters long")

    def verify_password(self, password):
        return self.__password == password

# Example usage
user = User("john_doe", "securePass123")
print(user.get_username())  # john_doe
print(user.verify_password("securePass123"))  # True
user.set_password("newSecurePass")