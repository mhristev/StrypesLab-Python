"""
Създайте програма, която отваря файл със stem (качен в Moodle) 
и ги вкарва в речник. 

Програмата с име XXXXX_L9_T2.py,  където XXXXX е вашето потребителско име в пощата, 
с която сте регистрирани, 

да получава параметри от командния ред (със sys.argv, не от клавиатурата) 
име на stem файл и дума. 

След попълване на речника да се проверява получената като параметър дума
за нейната основна форма и да се извежда резултата в стандартния изход.

"""

import sys

def load_stem_file(filename):
    stem_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            word, stem = line.strip().split(':')
            stem_dict[word] = stem
    return stem_dict

def find_base_form(word, stem_dict):
    if word in stem_dict:
        return stem_dict[word]


filename, word = sys.argv[1], sys.argv[2]

stem_dict = load_stem_file(filename)

print(find_base_form(word, stem_dict))