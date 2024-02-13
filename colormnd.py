
def colorize(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def black(text):
    return colorize(text, 30)


def red(text):
    return colorize(text, 31)


def green(text):
    return colorize(text, 32)


def yellow(text):
    return colorize(text, 33)


def blue(text):
    return colorize(text, 34)


def magenta(text):
    return colorize(text, 35)


def cyan(text):
    return colorize(text, 36)


def white(text):
    return colorize(text, 37)


def gray(text):
    return colorize(text, 90)


def bright_black(text):
    return colorize(text, 90)


def bright_red(text):
    return colorize(text, 91)


def bright_green(text):
    return colorize(text, 92)


def bright_yellow(text):
    return colorize(text, 93)


def bright_blue(text):
    return colorize(text, 94)


def bright_magenta(text):
    return colorize(text, 95)


def bright_cyan(text):
    return colorize(text, 96)


def bright_white(text):
    return colorize(text, 97)
