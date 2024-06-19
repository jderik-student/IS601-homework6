# pylint: disable=unnecessary-dunder-call, invalid-name, unnecessary-pass
'''
    Defines the logic for a Command and the CommandHandler to register and execute these commands
'''

from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation
from typing import List

class Command(ABC):
    """
        Abstract class that defines what a Command is
    """
    @abstractmethod
    def execute(self, user_input: List[Decimal]):
        """
            Abstract method that will be overriden by its subclasses to define Command execution

            @param user_input: a list of Decimals specified by the user, expectation is that there should be either zero or two elements in the list
        """
        pass # pragma: no cover

class CommandHandler:
    """
        This class will be used by the application to register and execute all REPL commands
    """
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command):
        """
            Adds a command to the CommandHandler's commands dictionary

            @param command_name: the name of the command
            @param command: the function to call when the command is typed by the user
        """
        self.commands[command_name] = command

    def list_commands(self):
        """
            Prints all the commands registered in the CommandHandler
        """
        print("Commands:")
        for key in self.commands:
            print(f"- {key}")

    def execute_command(self, user_input: List[str]):
        """
            Based on user input from the REPL, will call the method associated with the command specified by the user with any user defined arguments
            Prints the result

            @param user_input: User command line input, with each value stored in its own element
        """
        try:
            if user_input:
                self.commands[user_input[0]].execute([Decimal(string) for string in user_input[1:3]])
        except IndexError:
            print("ERROR Usage: <operation> <number1> <number2>")
        except ValueError:
            print("Cannot divide by zero")
        except InvalidOperation:
            print(f"Invalid number input: {user_input[1]} or {user_input[2]} is not a valid number.")
        except KeyError:
            print(f"No such command: {user_input[0]}")
        except Exception as e: # Catch-all for unexpected errors
            print(f"An error occurred: {e}") # pragma: no cover
