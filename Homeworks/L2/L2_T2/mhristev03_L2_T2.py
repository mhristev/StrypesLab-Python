import sys

def are_anagrams(str1, str2):
    word1, word2 = str1.lower().replace(" ", ""), str2.lower().replace(" ", "")
    return sorted(word1) == sorted(word2)

print(are_anagrams(sys.argv[1], sys.argv[2]))