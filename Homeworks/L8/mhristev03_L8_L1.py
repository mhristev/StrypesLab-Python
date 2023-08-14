""" 
Напишете програма, която намира корен на уравнения по метода на дихотомията.

Функцията f(x) да е изнесена в програмна структура функция за леснa промяна.

Числата a и b, които задават интервала на търсене да се въвеждат от клавиатурата. 
Числата да се четат като символен низ и след това да се конвертират до число.

Ако въведените от потребителя стойности не са числа, както и ако f(a) и f(b) 
имат един и същ знак да се пораждат съответни изключения.

Търсенето също да е изнесено във функция с име bisection, 
която получава три параметъра - a, b и функцията за изчисление f(x). 
След тестване оставете главната програма празна. 

Функцията bisection трябва да връща резултата с точност 0.001. 
Тя не трябва да печата нищо.

def f(x):
    return x*x*x+3*x-5


def bisection(a,b, func):
    ...
    ...
    ...
    return ...

print bisection(1,2, f)

Намерете корен на exp(x)-2x-2
Намерете корен на x^3 + 3x-5;

Програмата да е с име XXXXX_L8_T1.py, 
където XXXXX е вашето потребителско име в пощата, с която сте регистрирани. 

"""

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
    return x**3+3*x-5.0

def f2(x):
    return exp(x)-2*x-2.0


def main():
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


if __name__ == "__main__":
    main()