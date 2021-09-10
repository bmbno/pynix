from linux_commands.date import Date
from linux_commands.pwd import PresentWorkingDirectory
from linux_commands.man import Manual
from linux_commands.grep import Grep
from linux_commands.diff import Difference
from linux_commands.rm import Remove
from linux_commands.clear import Clear
from linux_commands.cp import Copy
from linux_commands.ls import DirectoryList
from linux_commands.mv import Move
from linux_commands.mkdir import MakeDirectory
from linux_commands.echo import Echo
from linux_commands.cd import CurrentDirectory
from linux_commands.exit import Exit


class Dos:
    def __init__(self, command):
        self.commands = {
            'ls': DirectoryList(),
            'mv': Move(),
            'cp': Copy(),
            'clear': Clear(),
            'rm': Remove(),
            'diff': Difference(),
            'grep': Grep(),
            'man': Manual(),
            'pwd': PresentWorkingDirectory(),
            'date': Date(),
            'cd': CurrentDirectory(),
            'mkdir': MakeDirectory(),
            'echo': Echo(),
            'exit': Exit()
        }
        self.command_key = command.split()[0]
        self.command = command

    def complete_translation(self):
        command_equiv = self.commands[self.command_key]
        translated_command = command_equiv.translate(self.command)

        return translated_command
