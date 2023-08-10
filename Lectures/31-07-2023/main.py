

# def caesar(text):
#     res = ""
#     for c in text:
#         if c.isupper():
#             res += chr((ord(c) + 3-ord('A')) % 26 + ord('A'))
#         elif c.islower():
#             res += chr((ord(c) + 3-ord('a')) % 26 + ord('a'))   
#         else:
#             res += c 
#     return res


def caesar(text):
    shift = 3
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alph = alph[shift:] + alph[:shift]
    table = str.maketrans(alph, shifted_alph)
    return text.translate(table)

# print(ord('a'))
# print(ord('A'))
print(caesar("HELLO, WORLD!"))



# keys = []
# for key, val in keys.items():
#     if val == value:
#         keys.append(key)
        
# return keys