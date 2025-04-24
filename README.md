# computorv1: Polynomial Equation Solver

## Description

This project is a Python-based polynomial equation solver that can parse and solve equations up to degree 2 (quadratic). It features:

- Equation parsing with support for various formats (e.g., `5 + 4X - X^2 = X^2`)
- Reduction to standard form (e.g., `-5 -4X + 2X^2 = 0`)
- Solution finding for:
  - Linear equations (degree 1)
  - Quadratic equations (degree 2)
  - Special cases (infinite solutions, no solution)
- Support for complex solutions
- Fraction simplification for exact solutions

## Features

- **Equation Parsing**: Handles multiple input formats including coefficients with/without operators
- **Solution Types**:
  - Real roots (rational and decimal)
  - Complex roots (with imaginary components)
  - Special cases (all real numbers, no solution)
- **Precision Handling**: Custom square root implementation with configurable precision
- **Error Handling**: Comprehensive validation of input equations

## Usage

Run the solver with test cases:
```bash
python3 test.py
```

Or integrate the solver into your code:
```python
from parsing import parse_equation

equation = parse_equation("X^2 + 1 = 0")
reduced_form = equation.reduce()
solution = equation.solve()
```

## Implementation Details

- **Newton's Method**: Used for square root approximation
- **Fraction Simplification**: GCD-based reduction for exact solutions
- **Polynomial Representation**: Stores terms in a dictionary by exponent
- **Error Checking**: Validates equation syntax and mathematical validity

## Example Output

For input `"5 + 4X - X^2 = X^2"`:
```
Reduced form: -5 -4X + 2X^2 = 0
Polynomial degree: 2
Quadratic equation: 2 * X² + -4 * X + -5 = 0
Discriminant Δ = b² - 4ac = -4² - 4*2*-5 = 56
Discriminant is strictly positive (Δ = 56), there are two real solutions:
√Δ ≈ 7.483314773547883
Solutions in decimal form:
X₁ ≈ 2.870829
X₂ ≈ -0.870829
```
