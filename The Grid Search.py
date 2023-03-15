def gridSearch(G, P):
    R = len(G)
    C = len(G[0])
    r = len(P)
    c = len(P[0])
    flag = False
    for i in range(R-r+1):
        for j in range(C-c+1):
            flag = False
            for k in range(r):
                for l in range(c):
                    if G[i+k][j+l] != P[k][l]:
                        flag = True
                        break
                if flag:
                    break
            if not flag:
                return "YES"
    return "NO"
