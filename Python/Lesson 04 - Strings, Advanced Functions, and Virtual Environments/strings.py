import re

password_accepted = False

while not password_accepted:
    user_password = input("Enter your password: ")
    if len(user_password) < 5 or len(user_password) > 15:
        password_accepted = False
        print("Password must be between 5 and 15 characters")
    elif not user_password[0].isalpha():
        password_accepted = False
        print("Password cannot start with a number")
    elif user_password[-1] == "_":
        password_accepted = False
        print("Password cannot end with an underscore")
    elif not any(char.isdigit() for char in user_password):
        password_accepted = False
        print("Password must contain a number")
    elif not bool(re.fullmatch(r"\w+", user_password)):
        password_accepted = False
        print("Password cannot contain special characters")
    else:
        password_accepted = True
        print("Password accepted")        
    