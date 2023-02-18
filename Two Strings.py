def twoStrings(s1, s2):
    for ch in s1:
        if ch in s2:
            return "YES"
    return "NO"

print(twoStrings("abc", "gjh"))