#!/usr/bin/env python3

import sys
from parsing import parse_equation

def main():
    if len(sys.argv) != 2:
        print("Usage: ./computor \"polynomial equation\"")
        return
    
    equation_str = sys.argv[1]
    
    try:
        equation = parse_equation(equation_str)
        reduced_form = equation.reduce()
        
        print(f"Reduced form: {reduced_form}")
        print(f"Polynomial degree: {equation.max_degree}")
        
        solution = equation.solve()
        print("\nSolving steps:")
        print(solution)
    
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
