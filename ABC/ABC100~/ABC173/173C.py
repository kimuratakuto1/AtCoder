H,W,K = map(int,input().split())
C = [list(input()) for _ in range(H)]

ans = 0
b = 0
rowcnt = [[] for i in range(H)]
colcnt = [[] for i in range(W)]
for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            b += 1
            rowcnt[i].append((i,j))
            colcnt[j].append((i,j))

for i in range(2**H):
    for j in range(2**W):
        check = []
        for k in range(6):
            if (i>>k)&1 == 1:
                check += (rowcnt[k])
        for l in range(6):
            if (j>>l)&1 == 1:
                check += (colcnt[l])
        if b-len(set(check)) == K:
            ans += 1
print(ans)
