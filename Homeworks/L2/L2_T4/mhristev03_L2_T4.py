import sys

def without_dups(lst):
    
    no_dups_lst = []
    
    for element in lst:
        if element not in no_dups_lst:
            no_dups_lst.append(element)
            
    return sorted(no_dups_lst)

print(without_dups(int(arg) for arg in sys.argv[1:]))