import sys


def confirm(message):
    answer = input(message).lower()
    if answer in ("y","yes"):
        return True
    elif answer in ("n","no"):
        return False
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
        return confirm(message)
