def matchingStrings(strings, queries):
    return [strings.count(q) for q in queries]

s = ["aba","baba","aba","xzxb"]
q = ["aba","xzxb","ab"]

print(matchingStrings(s, q))