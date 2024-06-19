# pylint: disable=unnecessary-dunder-call, invalid-name
"""
    Class used to store and access past Calculations that were inputted into the Calculator.
    The most recent Calculation would appear at the end of the list
"""

from typing import List
from app.calculator.calculation import Calculation

class CalculatorHistory:
    """
        Class used to store and access past Calculations that were inputted into the Calculator.
        The most recent Calculation would appear at the end of the list
    """
    history: List[Calculation] = []

    @classmethod
    def append(cls, calculation: Calculation):
        """
            Adds a Calculation to the history at the end of the list

            @param calculation: the Calculation to add to the history
        """
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """
            Returns the Calculation at the end of the history list.

           @return: the most recent Calculation (the Calculation at the end of the history list), returns None if the history is empty
        """
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """
            Returns the entire history

           @return: a list of all Calculations in the history
        """
        return cls.history

    @classmethod
    def delete_history(cls):
        """
           Clears all Calculations stored in the history list
        """
        cls.history.clear()

    @classmethod
    def find_by_opreation(cls, operation_name: str) -> List[Calculation]:
        """
           Finds and returns a list of all the Calculations wiht a specific operation

           @param operation_name: the desired operation to find
           @return: a list of Calculations with the speicified operation type
        """
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]

    @classmethod
    def get_ith_calculation(cls, i: int) -> Calculation:
        """
           Gets the ith Calculation in the history and returns it

           @param i: the desired position of the Caluclation to be retrieved
           @return: the Calculation at position i
        """
        return cls.history[i]
