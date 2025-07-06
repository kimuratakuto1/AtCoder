N,Q = map(int,input().split())
d = {i+1:[] for i in range(N)}
ans = []
f = [Q-1,0]
querylist = []
for i in range(Q):
    query = list(input().split())
    querylist.append(query)

for i in range(Q):
    query = querylist[-i-1]

    if int(query[0]) == 1:
        p = int(query[1])
        if f[1] == p:
            f = [f[0]-1,0]

    elif int(query[0]) == 2:
        p = int(query[1])
        s = query[2]
        if f[1] == p:
            ans.append(s)
            f = [f[0]-1,f[1]]
    else:
        p = int(query[1])
        if f[1] == 0:
            f = [f[0]-1,p]
for i in range(len(ans)):
    print(ans[-1-i],end="")
