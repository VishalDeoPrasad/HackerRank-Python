def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_home = 0
    oranges_home = 0
    # for apple in apples:
    #     #apple_home.append(a+apple)
    #     if a+apple >= s and a+apple<=t:
    #         apple_home += 1

    # for orange in oranges:
    #     #oranges_home.append(b+orange)
    #     if b+orange >=s and b+orange <=t:
    #         oranges_home += 1
    
    [apple_home := apple_home + 1 for apple in apples if a+apple >= s and a+apple<=t]
    [oranges_home := oranges_home + 1 for orange in oranges if b+orange >=s and b+orange <=t]
    print(apple_home, oranges_home)

    
countApplesAndOranges(7, 13, 4, 12, [2, 3, -4], [3, -2, -4])