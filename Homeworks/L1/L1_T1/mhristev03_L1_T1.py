import sys
import math

def solve_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            return "special case"
        x = -c/b
        return x
    
    D = b**2 - 4*a*c
    
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return f"{x1}|{x2}"
    elif D == 0:
        x = -b / (2*a)
        return x
    else:
        return "no real roots"
    
a, b, c = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

print(solve_quadratic_equation(a, b, c))