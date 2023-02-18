from collections import Counter

def gameOfThrones(s):
    dic_s = Counter(s)
    print(dic_s)
    cnt = 0
    for value in dic_s.values():
        cnt += value%2
    return "NO" if cnt > 1 else "YES"

print(gameOfThrones("aaabbbb"))