# pylint: disable=unnecessary-dunder-call, invalid-name
'''
    Defines the REPL command to get and print the Calculator's History
'''
from decimal import Decimal
from typing import List
from app.commands import Command
from app.calculator import CalculatorHistory

class GetHistoryCommand(Command):
    """
        This class extends the Abstract Command Class and gets and prints all calcualtions from the Calculator's History
    """
    def execute(self, user_input: List[Decimal]):
        """
            Gets and prints all calculations from the Calculator's History

            @param user_input: not used by this method, added to adhere to Liskov substitution principle
        """
        i = 1
        for calc in CalculatorHistory.get_history():
            print(f"{i}) {calc}")
            i += 1
