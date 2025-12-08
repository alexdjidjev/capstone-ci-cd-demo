import math


# Basic Operations
def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Advanced Operations
def logarithm(a, base=math.e):
    """Calculate logarithm of a with given base. Raises ValueError if a <= 0."""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    if base == math.e:
        return math.log(a)
    return math.log(a, base)


def square(a):
    """Calculate the square of a number."""
    return a ** 2


def sine(a):
    """Calculate sine of a (in radians)."""
    return math.sin(a)


def cosine(a):
    """Calculate cosine of a (in radians)."""
    return math.cos(a)


def square_root(a):
    """Calculate square root of a. Raises ValueError if a < 0."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)


def percentage(part, whole):
    """Calculate what percentage 'part' is of 'whole'. Raises ValueError if whole is zero."""
    if whole == 0:
        raise ValueError("Cannot calculate percentage with zero as whole")
    return (part / whole) * 100