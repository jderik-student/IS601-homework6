# pylint: disable=unnecessary-dunder-call, invalid-name, unused-variable, unused-argument
'''
    This file contains tests to test the all the Commands in the commands directory except the ExitCommand which is tested in test_app.py
'''

from decimal import Decimal
import pytest

from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.getHistory import GetHistoryCommand
from app.plugins.clearHistory import ClearHistoryCommand
from app.plugins.menu import MenuCommand
from app.calculator.calculation import Calculation
from app.calculator.calculatorHistory import CalculatorHistory
from app.calculator.operations import add, subtract, multiply, divide

@pytest.fixture(name="setup")
def setup_history():
    """First clears the history and setups the history for required tests"""
    CalculatorHistory.delete_history()
    CalculatorHistory.append(Calculation.create(Decimal('1'), Decimal('2'), divide))
    CalculatorHistory.append(Calculation.create(Decimal('3'), Decimal('4'), multiply))
    CalculatorHistory.append(Calculation.create(Decimal('5'), Decimal('6'), subtract))
    CalculatorHistory.append(Calculation.create(Decimal('7'), Decimal('8'), add))


def test_add_command(capfd):
    """Tests the AddCommand"""
    command = AddCommand()
    command.execute([Decimal(1), Decimal(2)])
    out, err = capfd.readouterr()
    assert out == "The result of 1 plus 2 is equal to 3\n", "The AddCommand should print 'The result of 1 plus 2 is equal to 3'"


def test_subtract_command(capfd):
    """Tests the SubtractCommand"""
    command = SubtractCommand()
    command.execute([Decimal(3), Decimal(2)])
    out, err = capfd.readouterr()
    assert out == "The result of 3 minus 2 is equal to 1\n", "The SubtractCommand should print 'The result of 3 minus 2 is equal to 1'"

def test_multiply_command(capfd):
    """Tests the MultiplyCommand"""
    command = MultiplyCommand()
    command.execute([Decimal(2), Decimal(4)])
    out, err = capfd.readouterr()
    assert out == "The result of 2 times 4 is equal to 8\n", "The MultiplyCommand should print 'The result of 2 times 4 is equal to 8'"

def test_divide_command(capfd):
    """Tests the DivideCommand"""
    command = DivideCommand()
    command.execute([Decimal(12), Decimal(4)])
    out, err = capfd.readouterr()
    assert out == "The result of 12 divided by 4 is equal to 3\n", "The DivideCommand should print 'The result of 12 divided by 4 is equal to 3'"

def test_get_history_command(setup, capfd):
    """Tests the GetHistoryCommand"""
    command = GetHistoryCommand()
    command.execute([])
    out, err = capfd.readouterr()
    assert out == "1) Calculation(1, 2, divide)\n2) Calculation(3, 4, multiply)\n3) Calculation(5, 6, subtract)\n4) Calculation(7, 8, add)\n", "The GetHistoryCommand should've printed 4 Calculations"

def test_clear_history_command(setup, capfd):
    """Tests the ClearHistoryCommand"""
    command = ClearHistoryCommand()
    command.execute([])
    command = GetHistoryCommand()
    command.execute([])
    out, err = capfd.readouterr()
    assert out == "", "The ClearHistoryCommand should have deleted the history"

def test_menu_command(capfd):
    """Tests the MenuCommand"""
    handler = CommandHandler()
    handler.register_command("Command1", None)
    handler.register_command("Command2", None)
    handler.register_command("Command3", None)
    command = MenuCommand(handler)
    command.execute([])
    out, err = capfd.readouterr()
    assert out == "Commands:\n- Command1\n- Command2\n- Command3\n", "The MenuCommand should have printed three commands"
