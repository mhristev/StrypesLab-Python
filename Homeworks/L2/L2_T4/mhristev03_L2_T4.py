import sys

def without_dups(lst):
    no_dups_lst = []
    
    for element in lst:
        if element not in no_dups_lst:
            no_dups_lst.append(element)
            
    return no_dups_lst

print(without_dups(sys.argv[1:]))