#!/usr/bin/env python3

import re
from polynomial_equation import PolynomialEquation

def parse_equation(equation_str):
    sides = equation_str.split('=')
    if len(sides) != 2:
        raise ValueError("Invalid equation format: must contain exactly one '=' sign")
    
    left_side, right_side = sides[0].strip(), sides[1].strip()
    
    if not left_side:
        raise ValueError("Left side of the equation cannot be empty")
    if not right_side:
        raise ValueError("Right side of the equation cannot be empty")
    
    equation = PolynomialEquation()
    
    parse_side(left_side, "left", equation)
    parse_side(right_side, "right", equation)
    
    return equation


def parse_side(expression, side, equation):

    expression = re.sub(r'\s*([+\-*^])\s*', r'\1', expression)

    if expression.endswith('+') or expression.endswith('-') or expression.endswith('*') or expression.endswith('^'):
        raise ValueError(f"Invalid equation format: '{expression}' ends with an operator")

   
    if '++' in expression:
        raise ValueError(f"Invalid equation format: consecutive '+' signs not allowed: '{expression}'")


    expression = expression.replace('-', '+-')

    if expression.startswith('+'):
        expression = expression[1:] 

    terms = expression.split('+')
    terms = [term for term in terms if term.strip()]
    
    if not terms:
        raise ValueError(f"The {side} side of the equation contains no valid terms")
    
    # 7) Parse each term
    for term in terms:
        if term.startswith('-'):
            coef_sign = -1
            term = term[1:]  # remove the leading '-'
        else:
            coef_sign = 1
        
        if not term:
            continue
        
        try:
            # Case 1: Just a number (e.g. "4", "-3.2")
            if term.replace('.', '', 1).isdigit():
                coef = float(term) * coef_sign
                exp = 0
                
            # Case 2: Just "X"
            elif term == 'X':
                coef = 1.0 * coef_sign
                exp = 1
                
            # Case 3: "X^n"
            elif term.startswith('X^'):
                coef = 1.0 * coef_sign
                exp_str = term[2:]
                exp = int(exp_str)  # throws ValueError if invalid
              
            # Case 4: "n*X" (coefficient = n, exponent=1)
            elif '*X' in term and '^' not in term:
                parts = term.split('*X')
                coef = float(parts[0]) * coef_sign
                exp = 1
                
            # Case 5: "n*X^m"
            elif '*X^' in term:
                parts = term.split('*X^')
                coef = float(parts[0]) * coef_sign
                exp = int(parts[1])
                
            # Case 6: "nX" (coefficient n, exponent=1)
            elif term.endswith('X'):
                coef_part = term[:-1]
                if not coef_part:  
                    coef = 1.0 * coef_sign
                else:
                    coef = float(coef_part) * coef_sign
                exp = 1
                
            # Case 7: "nX^m"
            elif 'X^' in term:
                parts = term.split('X^')
                coef_part = parts[0]
                if not coef_part:  # means the term was just "X^m"
                    coef = 1.0 * coef_sign
                else:
                    coef = float(coef_part) * coef_sign
                exp = int(parts[1])
                
            else:
                # If none of the patterns match, it's invalid syntax
                raise ValueError(f"Invalid term format: '{term}'")
            
            # Add the (coefficient, exponent) to the polynomial
            equation.add_term(coef, exp, side)
            
        except (ValueError, IndexError) as e:
            raise ValueError(f"Error parsing term '{term}': {str(e)}")
