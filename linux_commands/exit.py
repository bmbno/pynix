class Exit():
    def translate(self, input):
        commands = input.split()
        if len(commands) == 1:
            return "exit"
        elif len(commands == 2 and type(commands[1]) == int):
            return f"{commands[0]} /B {commands[1]}"
        else:
            return 0
