from src.utils.maths_utils import add, substract, multiply, divide

# Create a test on additions
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

# Create a test on substractions
def test_substract():
    assert substract(2,3) == -1
    assert substract(-1,1) == -2

# Create a test on multiplications
def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(-1,1) == -1

# Create a test on divisions
def test_divide():
    assert divide(2,3) == 2/3
    assert divide(-1,1) == -1

# Create a test on divisions by 0
def test_divide_by_zero():
    try:
        divide(5,0)
    except ValueError as e:
        assert str(e) == "Division by 0"