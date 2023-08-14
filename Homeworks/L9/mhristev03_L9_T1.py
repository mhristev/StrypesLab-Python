"""
Създайте програма, която отваря текстов файл и му сортира редовете, 
записвайки сортираните редове в друг файл. Програмата с име XXXXX_L9_T1.py,  
където XXXXX е вашето потребителско име в пощата, с която сте регистрирани, 
да получава параметри от командния ред (със sys.argv, не от клавиатурата) 
име на файл за сортиране и име на файл за записване на резултата.

"""
import sys

def sort_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    formated_lines = [item.strip() + '\n' for item in lines]
    sorted_lines = sorted(formated_lines)
    sorted_lines[-1] = sorted_lines[-1].rstrip('\n')
    
    print(sorted_lines)
    with open(output_file, 'w') as file:
        file.writelines(sorted_lines)
    

sort_lines(sys.argv[1], sys.argv[2])