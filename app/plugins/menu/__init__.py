# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    Defines the REPL command to print all available Commands registered in the Command Handler
'''
from decimal import Decimal
from typing import List
from app.commands import Command
from app.commands import CommandHandler


class MenuCommand(Command):
    """
        This class extends the Abstract Command Class and prints all the available Commands registered in the Command Handler
    """
    def __init__(self, command_handler: CommandHandler):
        """
            Passes in the command handler to be used by the execute method

            @param command_handler: the command handler used by the program
        """
        self.command_handler = command_handler

    def execute(self, user_input: List[Decimal]):
        """
            Prints all available Commands registered in the Command Handler

            @param user_input: not used by this method, added to adhere to Liskov substitution principle
        """
        self.command_handler.list_commands()
