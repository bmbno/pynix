class Exit():
    def translate(self, command):
        commands = command.split()
        command_key = commands[0]
        try:
            code = int(commands[1])
            return f"{command_key} /B {code}"
        except:
            if len(commands) == 1:
                return command
            return "echo 'ERROR: code must be a number'"
