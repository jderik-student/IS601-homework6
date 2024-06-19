# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    Defines the REPL command to add two decimal numbers together
'''

from decimal import Decimal
import logging
from typing import List
from app.commands import Command
from app.calculator import Calculator

class AddCommand(Command):
    """
        This class extends the Abstract Command Class and preforms addition based on user input
    """
    def execute(self, user_input: List[Decimal]):
        """
            Adds the first two Decimals defined in the user_input list and prints the result of the calculation

            @param user_input: a list of Decimals to be added specified by the user, expectation is that there should be only two elements in the list
        """
        result = Calculator.add(user_input[0], user_input[1])
        logging.debug("The result of %s plus %s is equal to %s", user_input[0], user_input[1], result)
        print(f"The result of {user_input[0]} plus {user_input[1]} is equal to {result}")
