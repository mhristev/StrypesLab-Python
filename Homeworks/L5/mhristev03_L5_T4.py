"""
Напишете рекурсивна функция, която връща дали даден символен низ е палиндром
(дали низът и обърнатият символен низ са същите).

Програмата да е с име XXXXX_L5_T4.py, 
където XXXXX е вашето потребителско име в пощата, с която сте регистрирани 
трябва да извежда True или False в завимиост от това дали входът е палиндром.
"""
import sys

def is_palindrome(txt):
    txt = txt.strip().lower()
    
    if len(txt) == 0:
        return True
    
    if txt[0] != txt[-1]:
        return False
    
    return is_palindrome(txt[1:-1])

print(is_palindrome(sys.argv[1]))
# print(is_palindrome('civic')) 
# print(is_palindrome('sagas'))
# print(is_palindrome('hello'))
# print(is_palindrome('')) 