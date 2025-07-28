# Create a function to add two numbers
def add(a : float, b : float) -> float:
    return a + b

# Create a function to substract a number from another one
def substract(a : float, b : float) -> float:
    return a - b

# Create a function to multiply two numbers
def multiply(a : float, b : float) -> float:
    return a * b 

# Create a function to divide two numbers
def divide(a : float, b : float) -> float:
    if b == 0:
        raise ValueError("Division by 0")
    return a / b