A = [list(map(int,input().split())) for _ in range(9)]

def rowcheck(X):
    for i in range(9):
        check = {j+1:False for j in range(9)}
        for k in range(9):
            if check[X[i][k]]:
                return False
            else:
                check[X[i][k]] = True
    return True
    

def colcheck(X):
    for i in range(9):
        check = {j+1:False for j in range(9)}
        for k in range(9):
            if check[X[k][i]]:
                return False
            else:
                check[X[k][i]] = True
    return True
    

def smallcheck(X):
    for i in range(3):
        for j in range(3):
            check = {j+1:False for j in range(9)}            
            for k in range(3):
                for l in range(3):
                    if check[X[i*3+k][j*3+l]]:
                        return False
                    else:
                        check[X[i*3+k][j*3+l]] = True
    return True

print("Yes" if rowcheck(A) == colcheck(A) == smallcheck(A) == True else "No")