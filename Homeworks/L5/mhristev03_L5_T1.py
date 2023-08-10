"""
Създайте рекурсивна функция за изчисляване на първите n числа на Фибоначи,
и тяхното съхранение в списък.

Реализацията трябва да съхранява вече изчислените стойности, 
така че когато рекурсивно извикване e c аргумент, който вече e изчислен, 
стойността да ce взима директно, a да не ce изчислява.  

Програмата с име XXXXX_L5_T1.py, където XXXXX e вашето потребителско име в пощата, 
c която сте регистрирани, да получава параметри от командния ред (със sys.argv, не от клавиатурата) 
начално и крайно число позиция в редицата и да разпечатва списък c числата от редицата на Фибоначи, 
от началният до крайният индекс включително.

Примерен изход при параметри 4 20:

[2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
"""

import sys

# def fib(n, mem={}):
#     # print(f'n = {n}')
#     if n in mem:
#         # print(f'I am in the dict with n = {n}')
#         return mem[n]
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0, 1]
    
#     prev_list = fib(n-1, mem)
#     prev_list.append(prev_list[-1] + prev_list[-2])
#     mem[n] = prev_list
    
#     return prev_list


def fib(n, mem={0:0, 1:1}):
    if n in mem:
        return mem[n]
    res = fib(n-1, mem) + fib(n-2, mem)
    mem[n] = res
    return res


bot_position, top_position = int(sys.argv[1]) - 1, int(sys.argv[2])

if bot_position < 0:
    bot_position = 0

print([fib(i) for i in range(bot_position, top_position)])