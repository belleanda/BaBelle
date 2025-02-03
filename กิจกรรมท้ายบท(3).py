class Authenticator:
    USERS = {"admin": "Ad13n@23t"}

    @staticmethod
    def login(username, password):
        username = username.lower()
        if username in Authenticator.USERS and Authenticator.USERS[username] == password:
            return "Welcome, admin"
        return "You are not admin"

user_input = input("Enter Username: ")
pass_input = input("Enter Password: ")

print(Authenticator.login(user_input, pass_input))