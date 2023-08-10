"""
Да се реализира на python алгоритъм за шифриране на Цезар. 
Програмата да приема като входни параметри от командния ред текст
и ключ и да извежда шифрирания текст в конзолата. 
Името на изпълнимия файл да е в следния формат: XXXXX_L3_T1.py,

"""
import sys

def caesar(txt, shift):
    alph_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alph_lower = "abcdefghijklmnopqrstuvwxyz"
    shifted_alph_upper = alph_upper[shift:] + alph_upper[:shift]
    shifted_alph_lower = alph_lower[shift:] + alph_lower[:shift]
    shifted_alph = shifted_alph_upper + shifted_alph_lower
    alph = alph_upper + alph_lower

    table = str.maketrans(alph, shifted_alph)
    return txt.translate(table)



print(caesar(sys.argv[1], int(sys.argv[2])))