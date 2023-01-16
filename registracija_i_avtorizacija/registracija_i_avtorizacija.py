from MyModule import * 

while True:
    choice = input("Do you want to register, login or exit? (register/login/exit) ")
    if choice.lower() == "register":
        register()
    elif choice.lower() == "login":
        login()
    elif choice.lower() == "exit":
        break
    else:
        print("Invalid choice.")