H,W = map(int,input().split())
s = [list(input()) for _ in range(H)]
t = [list(input()) for _ in range(H)]

S = [[] for _ in range(W)]
T = [[] for _ in range(W)]
for i in range(H):
    for j in range(W):
        S[j].append(s[i][j])
        T[j].append(t[i][j])

Sdict = {}
for i in range(W):
    if tuple(S[i]) in Sdict:
        Sdict[tuple(S[i])] += 1
    else:
        Sdict[tuple(S[i])] = 1
for i in range(W):
    if tuple(T[i]) in Sdict:
        if Sdict[tuple(T[i])] == 0:
            print("No")
            exit(0)
        else:
            Sdict[tuple(T[i])] -= 1
    else:
        print("No")
        exit(0)
print("Yes")