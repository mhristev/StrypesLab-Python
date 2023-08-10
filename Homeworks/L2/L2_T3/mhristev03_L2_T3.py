import sys

def has_dups(lst):
    found_elements = []
    for i in lst:
        if i in found_elements:
            return True
        found_elements.append(i)
    
    return False

print(has_dups(sys.argv[1:]))