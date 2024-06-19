# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    Defines the REPL command to multiply two decimal numbers together
'''

from decimal import Decimal
import logging
from typing import List
from app.commands import Command
from app.calculator import Calculator

class MultiplyCommand(Command):
    """
        This class extends the Abstract Command Class and preforms multiplication based on user input
    """
    def execute(self, user_input: List[Decimal]):
        """
            Multiplies the first two Decimals defined in the user_input list and prints the result of the calculation

            @param user_input: a list of Decimals to be multiplied specified by the user, expectation is that there should be only two elements in the list
        """
        result = Calculator.multiply(user_input[0], user_input[1])
        logging.debug("The result of %s times %s is equal to %s", user_input[0], user_input[1], result)
        print(f"The result of {user_input[0]} times {user_input[1]} is equal to {result}")
