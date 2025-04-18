#!/usr/bin/env python3
        
def custom_sqrt(x, epsilon=1e-10, max_iterations=100):
    
    if x < 0:
        return 0
    
    if x == 0:
        return 0
    
    if x == 1:
        return 1
    
    if x < epsilon:
        return x
    
    if x > 1e10:
        guess = x / 1e5
    else:
        guess = x / 2
    
    iterations = 0
    
    while iterations < max_iterations:
        # Newton-Raphson iteration: next = guess - f(guess)/f'(guess)
        # For sqrt(x), f(y) = y² - x, f'(y) = 2y
        
        if abs(guess) < epsilon:
            guess = epsilon
            
        next_guess = 0.5 * (guess + x / guess)
        
        # Check convergence
        if abs(next_guess - guess) < epsilon:
            return next_guess
        
        guess = next_guess
        iterations += 1
    
    return guess


# def binary_search_sqrt(x, epsilon=1e-10):
#     """
#     Fallback square root implementation using binary search.
#     More reliable but slower than Newton's method.
#     """
#     if x < 0:
#         return 0
#     if x == 0:
#         return 0
#     if x == 1:
#         return 1
    
#     # Establish search range
#     low = 0
#     high = max(1, x)  # Start with higher bound if x > 1
    
#     # Expand range if needed
#     while high * high < x:
#         high *= 2
    
#     # Binary search
#     while high - low > epsilon:
#         mid = (low + high) / 2
#         mid_squared = mid * mid
        
#         if abs(mid_squared - x) < epsilon:
#             return mid
#         elif mid_squared < x:
#             low = mid
#         else:
#             high = mid
    
#     return (low + high) / 2