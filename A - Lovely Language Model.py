N,M,L = map(int,input().split())
S = []
P = []
for i in range(N):
    sp = list(input().split())
    S.append(sp[0])
    P.append(int(sp[1]))

alf = { "a": 0, "b": 1, "c": 2, "d": 3,"e": 4,"f": 5 }
count = [[0 for i in range(6)] for i in range(6)]

for i in range(N):
    for j in range(len(S[i])-1):
        count[alf[S[i][j]]][alf[S[i][j+1]]] += 1

for i in alf:
    ans = []
    ans.append(i)
    p = sum(count[alf[i]])*2
    fin = 100
    for j in range(5):
        add = (100*count[alf[i]][j])//p
        ans.append(add)
        ans.append(add)
        fin -= add*2
    ans.append(fin//2)
    ans.append(fin//2)
    print(*ans)
    print(*ans)