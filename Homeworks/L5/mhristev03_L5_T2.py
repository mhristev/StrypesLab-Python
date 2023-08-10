"""
Създайте рекурсивна функция, която при зададено число и степен, 
връща числото, повдигнато на степента. 

Програмата с име XXXXX_L5_T2.py, където XXXXX е вашето потребителско име в пощата, 
с която сте регистрирани, да получава параметри от командния ред  (със sys.argv, не от клавиатурата) 
число и степен и да изпечатва резултатът от повдигането на числото на съответната степен.

Примерен изход при извикване с параметри 2 10:
1024
"""
import sys 

def pow(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * pow(a, n-1)
    else:
        return 1 / pow(a, -n)
    
print(pow(float(sys.argv[1]), float(sys.argv[2])))