
from colormnd import *
from loading import loading_dot


def login():
    try:
        input_username = input(blue("Enter Your Username: "))
        input_username = input_username.strip().lower()

        if input_username == "":
            print(red("You must enter a username (a-z, א - ת, 0-9)"))
            print()
            return main()

        list_options = "abcdefghijklmnopqrstuvwxyzאבגדהוזחטיכלמנסעפצקרשת0123456789"

        for char in input_username:
            if char not in list_options:
                print()
                print(red("You must enter a username (a-z, א - ת, 0-9)"))
                print()
                return main()

        input_password = input(blue("Enter Your Password: "))
        input_password = input_password.strip().lower()
        print()

        if input_password == "":
            print(red("You must enter a password (a-z, א - ת, 0-9)"))
            print()
            return main()

        first_note = input_username[0]

        path_username = f"users/{first_note}/{input_username}.txt"

        with open(path_username, "r") as file:

            password = file.read()
        if input_password == password:
            loading_dot(0.5, 3)
            print()

            import webbrowser
            webbrowser.open("https://www.youtube.com/watch?v=hPr-Yc92qaY")

            with open("status/mode_user.txt", "w") as file:
                file.write("on")
                file.write(f'\n{input_username}')
                file.write(f'\n{password}')

            with open("status/mode_user.txt", "r") as file:
                mode_ = file.readline().strip()
                username_ = file.readline().strip()
                password_ = file.readline().strip()

                if mode_ == "on" and username_ == input_username and password_ == input_password:
                    print()
                    main()

        else:
            print(red("The User Or Password Is wrong"))
            print()
            return main()

    except FileNotFoundError:
        print(red("The User Or Password Is wrong"))
        print()
        return main()


def sign_up():
    input_username = input(green("Create Username: "))

    list_options = "abcdefghijklmnopqrstuvwxyzאבגדהוזחטיכלמנסעפצקרשת0123456789"

    for char in input_username:
        if char not in list_options:
            print()
            print(red("You must enter a username (a-z, א - ת, 0-9)"))
            print()
            return main()

    input_password = input(green("Create Password: "))
    input_password_test = input(green("Enter password again: "))
    if input_password != input_password_test:
        print(red("The passwords do not match. "))
        return main()

    from os import path
    if path.isfile(f"users/{input_username[0]}/{input_username}.txt"):
        print(red("Username Already Exists"))
        print()
        return main()

    with open(f"users/{input_username[0]}/{input_username}.txt", "w") as file:
        file.write(input_password)

    main()


def log_out():
    with open(f"status/mode_user.txt", "r") as file:
        status = file.readline().strip()

        username = file.readline().strip()
        username = bright_cyan(username.strip().upper())

        if status == "off":
            print(red("You are not connected to any user"))
            print()
            return main()

        hyphen = yellow("-")
        print(red(f"You have exited the user {hyphen}{username}{hyphen}"))

        with open("status/mode_user.txt", "w") as file_:
            file_.write("off")
            main()

    if status == "off":
        mode_user_off()


def main():
    mode_user()

    desktop_login = blue("Login")
    desktop_sign_up = green("Sign up")
    desktop_log_out = red("Log out")
    desktop_exit = gray("exit()")

    selection_list = f"{desktop_login}, {desktop_sign_up}, {desktop_log_out}, {desktop_exit}"

    choose_an_option = input(f"Please enter one of the following options [{selection_list}]: ")
    choose_an_option = choose_an_option.lower()
    print()

    if choose_an_option == "login":
        login()

    elif choose_an_option == "sign up":
        sign_up()

    elif choose_an_option == "log out":
        log_out()

    elif choose_an_option == "exit()":
        exit()

    else:
        print(red("Input does not exist"))
        print()
        return main()


def mode_user_off():
    with open("status/mode_user.txt", "w") as file:
        file.write("off")


def mode_user():
    with open("status/mode_user.txt", "r") as file:
        mode = file.readline().strip()
        username = file.readline().strip()
        password = file.readline().strip()

        if username != '':
            import os

            if mode == "off":
                mode_user_off()

            if mode == "on":
                if os.path.exists(f"users/{username[0]}/{username}.txt"):
                    with open(f"users/{username[0]}/{username}.txt", "r") as file_:
                        search_password = file_.readline().strip()

                        if password == search_password:
                            username = bright_cyan(username.strip().upper())

                            hyphen = yellow("-")
                            print(magenta(f"You are connected to the user {hyphen}{username}{hyphen} "))

                        else:
                            mode_user_off()
                else:
                    mode_user_off()

        else:
            mode_user_off()


main()
