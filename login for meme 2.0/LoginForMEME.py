
from colormnd import *
from loading import loading_dot


def login():
    try:
        input_username = input(blue("Enter Your Username: "))
        input_username = input_username.strip().lower()

        if input_username == "":
            print(red("You must enter a username (a-z, א - ת, 0-9)"))
            main()

        input_password = input(blue("Enter Your Password: "))
        input_password = input_password.strip().lower()
        print()

        first_note = input_username[0]

        with open(f"users/{first_note}/{input_username}.txt", "r") as file:

            password = file.read()
        if input_password == password: 
            loading_dot(0.5, 5)
            print()

            import webbrowser
            webbrowser.open("https://www.youtube.com/watch?v=hPr-Yc92qaY")
            with open("status/mode_user.txt", "w") as file:
                file.write("on")
                file.write(f'\n{input_username}')
                file.write(f'\n{password}')

                with open("status/mode_password.txt", "r") as file_:
                    read = file_.read()
                    print(read)

                main()

        else:
            print(red("The User Or Password Is Incorrect"))
            print()
            return main()

    except FileNotFoundError:
        print(red("Username Not Found."))
        print()


def sign_up():
    input_username = input(green("Create Username: "))
    if input_username == "":
        print(red("You must enter a username for sign up(a-z, a-t, 0-9)"))

    input_password = input(green("Create Password: "))
    print()

    from os import path
    if path.isfile(f"users/{input_username[0]}/{input_username}.txt"):
        print(red("Username Already Exists"))
        print()
        return main()

    with open(f"users/{input_username[0]}/{input_username}.txt", "w") as file:
        file.write(input_password)

    main()


def log_out():
    with open(f"status/mode_user.txt", "w") as file:
        file.write("off")
        desktop()


def desktop():
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
        text_of_mode_user = file.read().strip()

        if username or password == "":
            mode_user_off()

        if text_of_mode_user == "":
            mode_user_off()

        if username != '':
            import os

            if mode == "on":
                if os.path.exists(f"users/{username[0]}/{username}.txt"):
                    with open(f"users/{username[0]}/{username}.txt", "r") as file_:
                        search_password = file_.readline().strip()

                        if password == search_password:
                            username = bright_red(username.strip().upper())
                            print(f"Hello -{username}- ")

                        else:
                            mode_user_off()
                else:
                    mode_user_off()


def main():
    mode_user()
    desktop()


main()
