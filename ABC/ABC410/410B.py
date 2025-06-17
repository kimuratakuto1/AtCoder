N,Q = map(int,input().split())
X = list(map(int,input().split()))
box = [0 for _ in range(N)]
ans = []
for i in range(Q):
    if X[i] == 0:
        for j in range(N):
            if box[j] == min(box):
                ans.append(j+1)
                box[j] += 1
                break
    else:
        ans.append(X[i])
        box[X[i]-1] += 1

print(*ans)
