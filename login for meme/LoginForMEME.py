# יבוא מקבצי python שאני כתבתי

from colormnd import red, green, blue       # יבוא צבעים
from loading import loading_dot         # יבוא טעינה


def login():
    try:
        # קלט שמשתמש וסיסמה
        input_username = input(green("Enter Your Username: "))
        input_password = input(green("Enter Your Password: "))
        print()

        with open(f"C:/Users/Jeloje8/Desktop/Projects/learn python/login for meme/users/{input_username}.txt", "r") as file:       # בדיקה האם השם משתמש קיים
            # אם המשתמש קיים בודקים האם הסיסמה תואמת
            password = file.read()
        if input_password == password: 
            loading_dot(0.5, 5)     # loading_dot(Time between point to point, Number of dots)
            print()
            # פתיחת המימ
            import webbrowser
            webbrowser.open("https://www.youtube.com/watch?v=hPr-Yc92qaY")

            # אם הסיסמה לא תואמת לקלט שגיאה וחזרה להתחלה
        else:
            print(red("The User Or Password Is Incorrect"))
            print()
            return main()
            # אם השמשתמש אינו קיים: שגיאה וחזרה להתחלה
    except FileNotFoundError:
        print(red("Username Not Found."))
        print() 


def sign_up():
    # קלט משתמש וסיסמה
    input_username = input(blue("Create Username: "))
    input_password = input(blue("Create Password: "))
    print()

    # בדיקה האם יש כבר משתמש באותו השמשתמש שנבחר. אם קיים: שגיאה וחזרה להתחלה
    from os import path
    if path.isfile(f"C:/Users/Jeloje8/Desktop/Projects/learn python/login for meme/users/{input_username}.txt"):
        print(red("Username Already Exists"))
        print()
        return main()

    # יצירת משתמש
    with open(f"C:/Users/Jeloje8/Desktop/Projects/learn python/login for meme/users/{input_username}.txt", "w") as file:    # מיקום שמירת משתמשים
        # הכנסת סיסמה לקובץ משתמש
        file.write(input_password)

    # חזרה להתחלה
    main()


def main():
    # צביעות בבחירות
    login_main = green("Login")
    sign_up_main = blue("Sign up")
    exit_main = red("exit()")

    # קלט בחירה
    choice = input(f"Choose one of the following options [{login_main}, {sign_up_main}, {exit_main}]: ")
    print()

    # הכוונה לפי הבחירה
    if choice == "login":
        login()

    elif choice == "sign up":
        sign_up()

    elif choice == "exit()":
        import sys
        sys.exit()

    else:   # אם הקלט אינו שווה לשום אחת מהאפשרויות: שגיאב וחזרה להתחלה
        print(red("Input does not exist"))
        print()
        return main()


# הפעלת main()
main()
