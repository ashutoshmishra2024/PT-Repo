import pytest

@pytest.mark.smoke
def test_addition(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0

@pytest.mark.smoke
def test_subtraction(calculator):
    assert calculator.subtract(1, 1) == 0
    assert calculator.subtract(-1, 1) == -2

@pytest.mark.regression
def test_multiplication(calculator):
    assert calculator.multiply(1, 2) == 2
    assert calculator.multiply(-1, 1) == -1

@pytest.mark.regression
def test_division(calculator):
    assert calculator.divide(10, 2) == 5.0
    # with pytest.raises(ValueError, match="Cannot divide by zero"):
    #     calculator.divide(10, 0)