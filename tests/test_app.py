# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    This file contains tests to test app.py
'''

import pytest
from app import App

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_full_app(capfd, monkeypatch):
    """Test that the goes through a sample workflow of the REPL app"""
    inputs = iter(['add 1 2', 'getHistory', 'subtract 3 1', 'divide 12 4', 'multiply 2 4',
                   'clearHistory', 'getHistory', 'menu', 'add', 'divide 1 0','add a b', 
                   'notACommand', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()

    captured = capfd.readouterr()
    assert "Type 'exit' to exit.\n" in captured.out
    assert "The result of 1 plus 2 is equal to 3\n" in captured.out
    assert "1) Calculation(1, 2, add)\n" in captured.out
    assert "The result of 3 minus 1 is equal to 2\n" in captured.out
    assert "The result of 12 divided by 4 is equal to 3\n" in captured.out
    assert "The result of 2 times 4 is equal to 8\n" in captured.out
    assert "The result of 3 minus 1 is equal to 2\n" in captured.out
    assert "\nCommands:\n" in captured.out
    assert "ERROR Usage: <operation> <number1> <number2>\n" in captured.out
    assert "Cannot divide by zero\n" in captured.out
    assert "Invalid number input: a or b is not a valid number.\n" in captured.out
    assert "No such command: notACommand\n" in captured.out
    assert e.type == SystemExit
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
