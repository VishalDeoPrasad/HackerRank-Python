from collections import Counter

def makingAnagrams(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)
    uniqe_char = (s1 - s2) + (s2 - s1)
    return sum(uniqe_char.values())

print(makingAnagrams("abc", "cde"))