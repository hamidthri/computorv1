#!/usr/bin/env python3

from collections import defaultdict
from custom_math import custom_sqrt

def simplify_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    if numerator == 0:
        return 0, 1
    
    # Find GCD (Greatest Common Divisor) inline
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    common_divisor = gcd(numerator, denominator)
    
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    
    # Ensure the denominator is positive
    if simplified_denominator < 0:
        simplified_numerator = -simplified_numerator
        simplified_denominator = -simplified_denominator
    
    return simplified_numerator, simplified_denominator


class PolynomialEquation:
    def __init__(self):
        self.terms = defaultdict(float)
        self.max_degree = 0
        self.reduced_form = ""
    
    def add_term(self, coefficient, exponent, side="left"):
        multiplier = 1 if side == "left" else -1
        self.terms[exponent] += coefficient * multiplier 
         
        if exponent > self.max_degree and abs(self.terms[exponent]) > 1e-10:
            self.max_degree = exponent
    
    def reduce(self):
        keys_to_remove = []
        for exp, coef in self.terms.items():
            if abs(coef) < 1e-10:
                keys_to_remove.append(exp)
        
        for key in keys_to_remove:
            del self.terms[key]
        
        if self.terms:
            self.max_degree = max(self.terms.keys())
        else:
            self.max_degree = 0
            self.terms[0] = 0
        
        terms_list = []
        for exp in sorted(self.terms.keys()):
            coef = self.terms[exp]
            if abs(coef) < 1e-10:
                continue
                
            if exp == 0:
                term = f"{coef}"
            elif exp == 1:
                term = f"{coef} * X"
            else:
                term = f"{coef} * X^{exp}"
                
            terms_list.append(term)
        
        if not terms_list:
            self.reduced_form = "0 = 0"
        else:
            self.reduced_form = " + ".join(terms_list).replace("+ -", "- ")
            self.reduced_form += " = 0"
        
        return self.reduced_form
    
    def solve(self):
        solution_steps = []
        
        if self.max_degree > 2:
            solution_steps.append("The polynomial degree is strictly greater than 2, I can't solve.")
            return "\n".join(solution_steps)
        
        if self.max_degree == 0:
            solution_steps.append(f"Equation: {self.reduced_form}")
            if abs(self.terms[0]) < 1e-10:
                solution_steps.append("All real numbers are solutions.")
            else:
                solution_steps.append("There is no solution.")
            return "\n".join(solution_steps)
        
        # --------------------------------------------
        # DEGREE 1: aX + b = 0 => X = -b/a
        # --------------------------------------------
        if self.max_degree == 1:
            solution_steps.append(f"Equation: {self.reduced_form}")
            a = self.terms.get(1, 0)
            b = self.terms.get(0, 0)
            
            solution_steps.append(f"Linear equation: {a} * X = -{b}")
            solution_steps.append(f"Solution is X = -({b}) / {a}")
            
            if abs(round(a) - a) < 1e-10 and abs(round(b) - b) < 1e-10:
                # Try fraction
                a_int = int(round(a))
                b_int = int(round(b))
                num, den = simplify_fraction(-b_int, a_int)
                if den == 1:
                    solution_steps.append(f"The solution is:\n{num}")
                else:
                    solution_steps.append(f"The solution is:\n{num}/{den}")
                    solution_steps.append(f"Which is approximately: {float(-b) / float(a)}")
            else:
                # Just do decimal
                solution = -b / a
                if abs(solution - round(solution)) < 1e-10:
                    solution = int(round(solution))
                solution_steps.append(f"The solution is:\n{solution}")
            
            return "\n".join(solution_steps)
        
        if self.max_degree == 2:
            solution_steps.append(f"Equation: {self.reduced_form}")
            a = self.terms.get(2, 0)
            b = self.terms.get(1, 0)
            c = self.terms.get(0, 0)
            
            solution_steps.append(f"Quadratic equation: {a} * X² + {b} * X + {c} = 0")
            
            discriminant = b**2 - 4*a*c
            solution_steps.append(
                f"Discriminant Δ = b² - 4ac = {b}² - 4*{a}*{c} = {discriminant}"
            )
            
            if abs(discriminant) < 1e-10:
                solution_steps.append("Discriminant is zero, there is one real solution:")
                solution = -b / (2*a)
                
                # fraction check
                if abs(round(2*a) - 2*a) < 1e-10 and abs(round(b) - b) < 1e-10:
                    a_int = int(round(a))
                    b_int = int(round(b))
                    num, den = simplify_fraction(-b_int, 2*a_int)
                    if den == 1:
                        solution_steps.append(f"X = {num}")
                    else:
                        solution_steps.append(f"X = {num}/{den}")
                        solution_steps.append(f"Which is approximately: {solution}")
                else:
                    if abs(solution - round(solution)) < 1e-10:
                        solution = int(round(solution))
                    solution_steps.append(f"X = {solution}")
            
            elif discriminant > 0:
                solution_steps.append(
                    f"Discriminant is strictly positive (Δ = {discriminant}), there are two real solutions:"
                )
                sqrt_discriminant = custom_sqrt(discriminant)
                solution_steps.append(f"√Δ ≈ {sqrt_discriminant}")
                
                sol1 = (-b + sqrt_discriminant) / (2*a)
                sol2 = (-b - sqrt_discriminant) / (2*a)
                
                if all(abs(round(x) - x) < 1e-10 for x in [a, b, sqrt_discriminant]):
                    a_int = int(round(a))
                    b_int = int(round(b))
                    disc_int = int(round(sqrt_discriminant))
                                        
                    
                    # X₁ = (-b + disc_int)/(2a)
                    num1 = -b_int + disc_int
                    den1 = 2 * a_int
                    num1_simp, den1_simp = simplify_fraction(num1, den1)
                    
                    # X₂ = (-b - √disc_int)/(2a)
                    num2 = -b_int - disc_int
                    den2 = 2 * a_int
                    num2_simp, den2_simp = simplify_fraction(num2, den2)
                    
                    solution_steps.append("Solutions in exact form:")
                    if den1_simp == 1:
                        solution_steps.append(f"X₁ = {num1_simp}")
                    else:
                        solution_steps.append(f"X₁ = {num1_simp}/{den1_simp}")
                    
                    if den2_simp == 1:
                        solution_steps.append(f"X₂ = {num2_simp}")
                    else:
                        solution_steps.append(f"X₂ = {num2_simp}/{den2_simp}")
                    
                else:
                    # Show decimal approximations
                    solution_steps.append("Solutions in decimal form:")
                    solution_steps.append(f"X₁ ≈ {round(sol1, 6)}")
                    solution_steps.append(f"X₂ ≈ {round(sol2, 6)}")
            
            else:
                solution_steps.append(
                    f"Discriminant is strictly negative (Δ = {discriminant}), there are two complex solutions:"
                )
                
                # real_part = -b/(2a)
                # imag_part = sqrt(|Δ|)/(2a)
                real_part_val = -b / (2*a)
                imag_val = custom_sqrt(abs(discriminant)) / (2*a)
                
                # We'll check if a, b are integers, and if |discriminant| is a perfect square.
                # That way, we can do a nice symbolic representation:  X = (real) ± sqrt(disc_abs)/something i
                # or a fraction if real part is fraction too.
                
                a_intlike = abs(round(a) - a) < 1e-10
                b_intlike = abs(round(b) - b) < 1e-10
                c_intlike = abs(round(c) - c) < 1e-10
                
                # Is -discriminant a near-integer perfect square?
                disc_abs = abs(discriminant)
                disc_abs_int = round(disc_abs)
                is_perfect_square = (abs(disc_abs_int - disc_abs) < 1e-10) and \
                                    (abs(round(custom_sqrt(disc_abs_int)) - custom_sqrt(disc_abs_int)) < 1e-10)
                
                if a_intlike and b_intlike and c_intlike:
                    a_int = int(round(a))
                    b_int = int(round(b))
                    
                    real_num, real_den = simplify_fraction(-b_int, 2*a_int)
                    
                    if is_perfect_square:
                        sqrt_val = int(round(custom_sqrt(disc_abs_int)))
                        
                        # E.g., imag_part = sqrt_val / (2a_int)
                        imag_num, imag_den = simplify_fraction(sqrt_val, 2*a_int)
                        
                        solution_steps.append("Solutions in exact form:")
                        
                        if real_den == 1:
                            real_part_str = f"{real_num}"
                        else:
                            real_part_str = f"{real_num}/{real_den}"
                        
                        if imag_den == 1:
                            imag_part_str = f"{imag_num}"
                        else:
                            imag_part_str = f"{imag_num}/{imag_den}"
                        
                        solution_steps.append(
                            f"X₁ = {real_part_str} + {imag_part_str}i"
                        )
                        solution_steps.append(
                            f"X₂ = {real_part_str} - {imag_part_str}i"
                        )
                        
                        solution_steps.append("\nApproximate solutions:")
                    else:
                        solution_steps.append("Solutions in exact form (symbolic):")
                        
                        if real_den == 1:
                            real_str = f"{real_num}"
                        else:
                            real_str = f"{real_num}/{real_den}"
                        
                        # Imag part is sqrt(disc_abs) / (2a)
                        # We can't simplify that further if it's not a perfect square,
                        # so let's represent it as sqrt(disc_abs_int) in symbolic form:
                        # i.e. "√(disc_abs_int)/(2a_int)"
                        
                        # But if disc_abs was not integer, we do '√(disc_abs)' anyway
                        # We'll do int(disc_abs_int) if it's near integer
                        disc_str = f"{disc_abs_int}" if abs(disc_abs_int - disc_abs) < 1e-10 else f"{disc_abs}"
                        
                        denom_str = f"{2*a_int}"
                        solution_steps.append(
                            f"X₁ = {real_str} + √({disc_str})/{denom_str} i"
                        )
                        solution_steps.append(
                            f"X₂ = {real_str} - √({disc_str})/{denom_str} i"
                        )
                        solution_steps.append("\nApproximate solutions:")
                else:
                    solution_steps.append("Solutions in decimal form:")
                
                re_rounded = round(real_part_val, 6)
                im_rounded = round(imag_val, 6)
                
                if abs(re_rounded - round(re_rounded)) < 1e-10:
                    re_rounded = int(round(re_rounded))
                if abs(im_rounded - round(im_rounded)) < 1e-10:
                    im_rounded = int(round(im_rounded))
                
                solution_steps.append(f"X₁ = {re_rounded} + {im_rounded}i")
                solution_steps.append(f"X₂ = {re_rounded} - {im_rounded}i")
            
            return "\n".join(solution_steps)
