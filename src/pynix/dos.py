from .linux_commands.exit import Exit

class Dos:
    def __init__(self, command):
        self.commands = {
            'ls': 'dir',
            'mv': 'ren',
            'cp': 'copy',
            'mv': 'move',
            'clear': 'cls',
            'rm': 'del',
            'diff': 'fc',
            'grep': 'find',
            'man': '/?',
            'pwd': 'chdir',
            'date': 'time',
            'cd': 'cd',
            'mkdir': 'md',
            'echo': 'echo',
            'exit':Exit()
        }
        self.command = command
    
    def translate(self, command):
        command_equiv = 0
        return command_equiv
