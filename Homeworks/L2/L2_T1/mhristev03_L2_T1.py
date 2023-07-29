import sys

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return "unsorted"
    return "sorted"

print(is_sorted(sys.argv[1:]))