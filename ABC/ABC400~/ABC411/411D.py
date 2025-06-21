N,Q = map(int,input().split())
d = {i+1:[] for i in range(N)}
S = []

for i in range(Q):
    query = list(input().split())

    if int(query[0]) == 1:
        p = int(query[1])
        d[p] = S

    elif int(query[0]) == 2:
        p = int(query[1])
        s = query[2]
        if d[p] == S:
            d[p] = d[p] + [s]
        else:
            d[p].append(s)

    else:
        p = int(query[1])
        S = d[p]
    print(d,S,i)
print("".join(S))