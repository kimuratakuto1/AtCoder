T = int(input())
for i in range(T):
    N = int(input())
    S = (input())
    d = []
    if N == 1:
        print(S)
    else:
        for l in range(N-1):
            for r in range(l+1,N):
                p = S[:l] + S[l+1:r+1] + S[l] + S[r+1:N]
                d.append(p)
        d.sort()
        print(d[0])