import platform
import os
from dos import Dos


def main():
    EXIT = 0
    _platform = platform.system()
    directory = os.path.expanduser("~")

    if _platform == "Windows":
        while EXIT == 0:
            command = input(f'{directory} $ ')
            if ('exit' in command):
                terminal = Dos(command)
                os.system(terminal.complete_translation())
                EXIT = 1
                break
            terminal = Dos(command)
            os.system(terminal.complete_translation())
    else:
        while EXIT == 0:
            command = input('$ ')
            if (command == 'exit'):
                EXIT = 1
            os.system(command)


if __name__ == '__main__':
    main()
