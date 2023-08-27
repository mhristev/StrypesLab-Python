from math import exp
def bisection_method(a, b, f):
    max_iterations = 10000
    tol = 0.001
    c = (a + b) / 2
    while abs(b - a) / 2 > tol and f(c) != 0:
        c = (a + b) / 2

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
            
    return c

def f(x):
    return x**3+3*x-5

def f2(x):
    return exp(x)-2*x-2

# root = bisection_method(1, 2, f)

# print("The root is around:", root)
# print("f(): ", f(root))

# root = bisection_method(1, 2, f2)
# print("Root 2 is around: ", root)
# print ("f2(): ", f2(root))