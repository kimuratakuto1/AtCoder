N = int(input())
D = list(map(int,input().split()))

for i in range(N-1):
    ans = []
    dist = 0
    for j in range(len(D)-i):
        dist += D[i+j]
        ans.append(dist)
    print(*ans)
    