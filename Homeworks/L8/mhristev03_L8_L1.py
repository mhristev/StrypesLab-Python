from math import exp

def bisection(a, b, f, tol=0.001, max_iterations=500):
    
    if a == b:
        raise ValueError("Initial interval has zero width.")
    
    if f(a) * f(b) > 0:
        raise ValueError("Function does not change sign within the initial interval.")
    
    iterations = 0
    c = (a + b) / 2.0

    while abs(b - a) / 2.0 > tol and f(c) != 0:

        c = (a + b) / 2.0
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iterations += 1
        if iterations >= max_iterations:
            raise ValueError("Bisection method did not converge within the maximum number of iterations.")
    
    return (c, iterations)

def f(x):
    return x**3+3*x-5

def f2(x):
    return exp(x)-2*x-2


max_attempts = 5  
attempt = 0

while attempt < max_attempts:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        root, iterations = bisection(a, b, f)
        print(f"Approximate root: {root}, iterations: {iterations}")
        print(f"Function value at root: {f(root)}")
        break 
    except ValueError as e:
        print(e)
        attempt += 1
        if attempt < max_attempts:
            print(f"You have {max_attempts - attempt} attempts remaining.\n")
        else:
            print("Maximum attempts reached. Exiting.")


