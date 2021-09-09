import platform
import os
from dos import Dos


def main():
    EXIT = 0
    _platform = platform.system()

    if _platform == "Windows":
        while EXIT == 0:
            command = input('$ ')
            if (command == 'exit'):
                EXIT = 1
            terminal = Dos(command)
            os.system(terminal.translate())
    else:
        while EXIT == 0:
            command = input('$ ')
            if (command == 'exit'):
                EXIT = 1
            os.system(command)


if __name__ == '__main__':
    main()