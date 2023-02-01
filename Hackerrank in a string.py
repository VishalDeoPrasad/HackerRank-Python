def hackerrankInString(s):
    # Write your code here
    string = "hackerrank"
    i = 0
    for c in s:
        if c == string[i]:
            i += 1 
            if i == len(string):
                return "YES"
    return "NO"

print(hackerrankInString("hhhaacckerrrannk"))