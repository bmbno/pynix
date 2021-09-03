import platform
import os


def main():
    EXIT = 0
    _platform = platform.system()

    if _platform == "Windows":
        while EXIT == 0:
            commands = input('$ ')
            if (commands == 'exit'):
                EXIT = 1
            # terminal = new Dos()
    else:
        while EXIT == 0:
            commands = input('$ ')
            if (commands == 'exit'):
                EXIT = 1
            os.system(commands)


if __name__ == '__main__':
    main()
