H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
grid = [[False]*W for _ in range(H)]
ans = 0

import sys
sys.setrecursionlimit(10**7)


def f(i,j,grid):
    global ans
    if i == H:
        ans = max(ans,XORcheck(grid,A))
        return
    if j == W:
        f(i+1,0,grid)
        return
    if grid[i][j]:#空いていない場合
        f(i,j+1,grid)
    else: #空いている場合
        f(i,j+1,grid)
        if j < W-1:
            if grid[i][j] == grid[i][j+1] == False: #横における場合
                grid[i][j] = grid[i][j+1] = True
                f(i,j+1,grid)
                grid[i][j] = grid[i][j+1] = False
        if i < H-1:
            if grid[i][j] == grid[i+1][j] == False: #縦における場合
                grid[i][j] = grid[i+1][j] = True
                f(i,j+1,grid)
                grid[i][j] = grid[i+1][j] = False


def XORcheck(grid,A):
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == False:
                count ^= A[i][j]
    return count
f(0,0,grid)
print(ans)