# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    Defines the REPL command to preform division on two decimal numbers
'''

from decimal import Decimal
import logging
from typing import List
from app.commands import Command
from app.calculator import Calculator

class DivideCommand(Command):
    """
        This class extends the Abstract Command Class and preforms division based on user input
    """
    def execute(self, user_input: List[Decimal]):
        """
            Preforms division on the first two Decimals defined in the user_input list and prints the result of the calculation

            @param user_input: a list of Decimals to be divided specified by the user, expectation is that there should be only two elements in the list
        """
        result = Calculator.divide(user_input[0], user_input[1])
        logging.debug("The result of %s divided by %s is equal to %s", user_input[0], user_input[1], result)
        print(f"The result of {user_input[0]} divided by {user_input[1]} is equal to {result}")
