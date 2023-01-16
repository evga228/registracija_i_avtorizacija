users = {}

def register():
    """Rgister
    :param any username: type username
    :param any password: tyme password
    """
    username = input("Enter a username: ")
    while True:
        choice = input("Do you want to generate a password automatically or enter it yourself? (auto/manual) ")
        if choice.lower() == "auto":
            import random
            import string
            password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
            print("Your password is: " + password)
            break
        elif choice.lower() == "manual":
            password = input("Enter a password: ")
            validate_password(password)
            if validate_password(password):
                print("Password is valid")
            else:
                print("Password is invalid")
            break
        else:
            print("Invalid choice.")
    users[username] = password
    print("Registration successful!")

def login()->any:
    """Login
    :param any username: type username
    :param any password: tyme password
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Incorrect username or password.")

def validate_password(password:any)->bool:
    """ Password check
    :param any password: type password
    :rtype: bool
    """
    if len(password) < 8:
        return False
    if not ("[a-z]", password):
        return False
    if not ("[A-Z]", password):
        return False
    if not ("[0-9]", password):
        return False
    if not ("[!@#\$%^&*()]", password):
        return False
    return True
