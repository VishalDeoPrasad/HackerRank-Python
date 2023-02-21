def luckBalance(k, contests):
    imp = []
    non_imp = []
    for points, value in contests:
        if value == 1:
            imp.append(points)
        if value == 0:
            non_imp.append(points)
    imp.sort(reverse=True)
    return sum(imp[:k])-sum(imp[k:])+sum(non_imp)

k=3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
print(luckBalance(k, contests))