N,L = map(int,input().split())
d = list(map(int,input().split()))

if L % 3 != 0:
    print(0)
else:
    ans = 0
    D = {i:[] for i in range(L)}
    place = 0
    D[0].append(1)
    for i in range(N-1):
        place += d[i]
        place %= L
        D[place].append(i+2)

    #iは正三角形の頂点のひとつ
    for i in range(L//3): 
        ans += len(D[i]) * len(D[i+L//3]) * len(D[i+L*2//3])
    print(ans)