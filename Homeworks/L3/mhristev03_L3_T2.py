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


def vigenere_encrypt(txt, key):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    res = ""
    key_index = 0  
    
    for char in txt:
        if char.isalpha():
            shift = alph.index(key[key_index % len(key)])
            res += caesar(char, shift)
            key_index += 1
        else:
            res += char
    
    return res

print(vigenere_encrypt(sys.argv[1], sys.argv[2]))

