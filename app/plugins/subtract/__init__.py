# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    Defines the REPL command to preform subtraction on two decimal numbers
'''

from decimal import Decimal
from typing import List
from app.commands import Command
from app.calculator import Calculator

class SubtractCommand(Command):
    """
        This class extends the Abstract Command Class and preforms subtraction based on user input
    """
    def execute(self, user_input: List[Decimal]):
        """
            Preforms subtraction on the first two Decimals defined in the user_input list and prints the result of the calculation

            @param user_input: a list of Decimals to be subtracted specified by the user, expectation is that there should be only two elements in the list
        """
        print(f"The result of {user_input[0]} minus {user_input[1]} is equal to {Calculator.subtract(user_input[0], user_input[1])}")
