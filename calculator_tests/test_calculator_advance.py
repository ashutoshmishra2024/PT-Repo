import pytest

@pytest.mark.advanced
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)

@pytest.mark.advanced
def test_float_operations(calculator):
    assert calculator.add(1.1, 2.2) == 3.3