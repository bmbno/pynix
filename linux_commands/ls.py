class DirectoryList:
    def __init__(self):
        flags = {}

    def translate(self, input):
        commands = input.split()
        if len(commands) == 1:
            return "dir"
        return
