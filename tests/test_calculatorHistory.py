# pylint: disable=unnecessary-dunder-call, invalid-name, unused-argument
'''
    This file contains tests to test the CalculationHistory class
'''

from decimal import Decimal
import pytest
from app.calculator.calculation import Calculation
from app.calculator.calculatorHistory import CalculatorHistory
from app.calculator.operations import add, subtract, multiply, divide

@pytest.fixture(name="setup")
def setup_history():
    """First clears the history and setups the history for each test"""
    CalculatorHistory.delete_history()
    CalculatorHistory.append(Calculation.create(Decimal('1'), Decimal('2'), add))
    CalculatorHistory.append(Calculation.create(Decimal('3'), Decimal('4'), subtract))
    CalculatorHistory.append(Calculation.create(Decimal('5'), Decimal('6'), multiply))
    CalculatorHistory.append(Calculation.create(Decimal('7'), Decimal('8'), divide))

def test_append(setup):
    """Test appending a Calculation to the history"""
    calculation = Calculation.create(Decimal('9'), Decimal('10'), add)
    CalculatorHistory.append(calculation)

    assert CalculatorHistory.get_last_calculation() == calculation, "Failed to append the Calculation to the history"

def test_get_last_calculation(setup):
    """Test getting the most recent calculation in the history"""
    last_calculation = CalculatorHistory.get_last_calculation()
    assert last_calculation.a == Decimal('7') and last_calculation.b == Decimal('8') and last_calculation.operation.__name__ == "divide", "Failed to get the correct most recent Calculation"

def test_get_last_calculation_with_empty_history():
    """Test getting the most recent calculation in the history with an empty history"""
    CalculatorHistory.delete_history()
    last_calculation = CalculatorHistory.get_last_calculation()
    assert last_calculation is None, "Expected None to be returned"

def test_get_history(setup):
    """Test getting the entire calculation history"""
    assert len(CalculatorHistory.get_history()) == 4, "History does not contain the expected number of calculations (4)"

def test_delete_history(setup):
    """Test deleting the entire calculation history"""
    CalculatorHistory.delete_history()
    assert len(CalculatorHistory.get_history()) == 0, "Failed to delete history"

def test_find_by_operation(setup):
    """Test getting the history by each opearation"""
    add_operation = CalculatorHistory.find_by_opreation("add")
    subtract_operation = CalculatorHistory.find_by_opreation("subtract")
    multiply_operation = CalculatorHistory.find_by_opreation("multiply")
    divide_operation = CalculatorHistory.find_by_opreation("divide")

    assert len(add_operation) == 1, "Did not find the correct number of calculations with the add operation"
    assert len(subtract_operation) == 1, "Did not find the correct number of calculations with the subtract operation"
    assert len(multiply_operation) == 1, "Did not find the correct number of calculations with the mulitply operation"
    assert len(divide_operation) == 1, "Did not find the correct number of calculations with the divide operation"

def test_get_ith_calculation(setup):
    """Test getting the ith Calculation in the history"""
    first_calculation = CalculatorHistory.get_ith_calculation(0)
    second_calculation = CalculatorHistory.get_ith_calculation(1)
    third_calculation = CalculatorHistory.get_ith_calculation(2)
    fourth_calculation = CalculatorHistory.get_ith_calculation(3)
    assert first_calculation.a == Decimal('1') and first_calculation.b == Decimal('2') and first_calculation.operation.__name__ == "add", "Failed to get the Calculation at index 0"
    assert second_calculation.a == Decimal('3') and second_calculation.b == Decimal('4') and second_calculation.operation.__name__ == "subtract", "Failed to get the Calculation at index 1"
    assert third_calculation.a == Decimal('5') and third_calculation.b == Decimal('6') and third_calculation.operation.__name__ == "multiply", "Failed to get the Calculation at index 2"
    assert fourth_calculation.a == Decimal('7') and fourth_calculation.b == Decimal('8') and fourth_calculation.operation.__name__ == "divide", "Failed to get the Calculation at index 3"
