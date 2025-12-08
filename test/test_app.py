import sys
from pathlib import Path
import math
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (
    add, subtract, multiply, divide,
    logarithm, square, sine, cosine, square_root, percentage
)


# Basic Operations Tests
def test_add_positive():
    assert add(5, 6) == 11

def test_add_negative():
    assert add(-5, -6) == -11

def test_add_mixed():
    assert add(5, -3) == 2

def test_add_zero():
    assert add(0, 0) == 0

def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(-10, -4) == -6

def test_subtract_mixed():
    assert subtract(5, 10) == -5

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_negative():
    assert multiply(-3, -4) == 12

def test_multiply_mixed():
    assert multiply(-3, 4) == -12

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_divide_positive():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-10, -2) == 5

def test_divide_mixed():
    assert divide(-10, 2) == -5

def test_divide_float():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# Advanced Operations Tests
def test_logarithm_natural():
    assert abs(logarithm(math.e) - 1.0) < 1e-10

def test_logarithm_base_10():
    assert abs(logarithm(100, 10) - 2.0) < 1e-10

def test_logarithm_base_2():
    assert abs(logarithm(8, 2) - 3.0) < 1e-10

def test_logarithm_zero():
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
        logarithm(0)

def test_logarithm_negative():
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
        logarithm(-5)

def test_square_positive():
    assert square(5) == 25

def test_square_negative():
    assert square(-5) == 25

def test_square_zero():
    assert square(0) == 0

def test_square_float():
    assert abs(square(2.5) - 6.25) < 1e-10

def test_sine_zero():
    assert abs(sine(0) - 0) < 1e-10

def test_sine_pi_over_2():
    assert abs(sine(math.pi / 2) - 1.0) < 1e-10

def test_sine_pi():
    assert abs(sine(math.pi) - 0) < 1e-10

def test_sine_negative():
    assert abs(sine(-math.pi / 2) - (-1.0)) < 1e-10

def test_cosine_zero():
    assert abs(cosine(0) - 1.0) < 1e-10

def test_cosine_pi_over_2():
    assert abs(cosine(math.pi / 2) - 0) < 1e-10

def test_cosine_pi():
    assert abs(cosine(math.pi) - (-1.0)) < 1e-10

def test_cosine_negative():
    assert abs(cosine(-math.pi) - (-1.0)) < 1e-10

def test_square_root_positive():
    assert square_root(16) == 4

def test_square_root_zero():
    assert square_root(0) == 0

def test_square_root_float():
    assert abs(square_root(2) - 1.4142135623730951) < 1e-10

def test_square_root_negative():
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        square_root(-4)

def test_percentage_basic():
    assert percentage(50, 200) == 25

def test_percentage_over_100():
    assert percentage(200, 100) == 200

def test_percentage_zero_part():
    assert percentage(0, 100) == 0

def test_percentage_same_values():
    assert percentage(50, 50) == 100

def test_percentage_zero_whole():
    with pytest.raises(ValueError, match="Cannot calculate percentage with zero as whole"):
        percentage(50, 0)