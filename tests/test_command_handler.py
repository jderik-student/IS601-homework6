# pylint: disable=unnecessary-dunder-call, invalid-name, unused-argument, unused-variable
'''
    This file contains tests to test the CommandHandler class
'''

from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand

def test_register_command_and_list_command(capfd):
    """Tests registering a command to the CommandHandler and listing out all the registered commands"""
    handler = CommandHandler()
    handler.register_command("add", AddCommand())
    handler.list_commands()
    out, err = capfd.readouterr()
    assert out == "Commands:\n- add\n", "Did not succesfully register and list out the AddCommand"

def test_execute_command(capfd):
    """Tests the execute_command method as well as the exceptions it catches"""
    handler = CommandHandler()
    handler.register_command("add", AddCommand())
    handler.register_command("divide", DivideCommand())

    handler.execute_command(["add", "1", "2"])
    out, err = capfd.readouterr()
    assert out == "The result of 1 plus 2 is equal to 3\n", "The AddCommand should print 'The result of 1 plus 2 is equal to 3'"

    handler.execute_command(["add"])
    out, err = capfd.readouterr()
    assert out == "ERROR Usage: <operation> <number1> <number2>\n", "IndexError was expected"

    handler.execute_command(["divide", "1", "0"])
    out, err = capfd.readouterr()
    assert out == "Cannot divide by zero\n", "ValueError was expected"

    handler.execute_command(["divide", "a", "b"])
    out, err = capfd.readouterr()
    assert out == "Invalid number input: a or b is not a valid number.\n", "InvalidOperation was expected"

    handler.execute_command(["notACommand", "1", "2"])
    out, err = capfd.readouterr()
    assert out == "No such command: notACommand\n", "KeyError was expected"
