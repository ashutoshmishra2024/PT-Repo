import pytest
from calculator_tests.calculator import Calculator

@pytest.fixture()
def calculator():
    return Calculator()