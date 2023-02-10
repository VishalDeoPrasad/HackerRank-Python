from collections import Counter
def commonStr(s1, s2):
    diff = Counter(s1) - Counter(s2)
    return sum(diff.values())
    
    
def anagram(s):
    # idea 1 - split string into half
    #      - find common element among them
    #      - return len(half string) - common element
    # idea 2 - Split string into half
    #      - find diff between 2 string and return
    n = len(s)
    if n % 2 != 0:
        return -1
    diff_char = commonStr(s[:n//2], s[n//2:])
    return diff_char

print(anagram("fdhlvosfpafhalll"))