def caesarCipher(s, k):
    # print(ord("a"), ord("z"), chr(97), chr(122))
    # print(ord("A"), ord("Z"), chr(65), chr(90))
    k = k%26
    new_s = ""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            if ord(c)+k <= 122:
                new_s += chr(ord(c)+k)
            else:
                diff = abs(ord(c)+k - 122)
                new_s += chr(96+diff)
        elif ord(c) >= 65 and ord(c) <= 90:
            if ord(c)+k <= 90:
                new_s += chr(ord(c)+k)
            else:
                diff = abs(ord(c)+k - 90)
                new_s += chr(64+diff)
        else:
            new_s += c
    return new_s

s1 = "There's-a-starman-waiting-in-the-sky"
s = 'www.abc.xy'  #fff.jkl.gh
k = 87
print(caesarCipher(s, k))