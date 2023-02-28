def towerBreakers(n, m):
    return 2 if m == 1 or n%2==0 else 1

print(towerBreakers(2,6))