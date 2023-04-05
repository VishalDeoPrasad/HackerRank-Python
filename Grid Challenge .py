def gridChallenge(grid):
    row, col = len(grid), len(grid[0])
    for i in range(row):
        grid[i] = list(grid[i])
        grid[i].sort()
    
    for i in range(col):
        for j in range(1, row):
            if grid[j][i] < grid[j-1][i]:
                return "NO"
    return "YES"
grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
print(gridChallenge(grid))