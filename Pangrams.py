def pangrams(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    print(s)
    for c in alpha:
        if c not in s:
            return "not pangram"
    return "pangram" 

s = 'We promptly judged antique ivory buckles for the next prize'
print(pangrams(s))