N,H,M = map(int,input().split())
a = [(H,M)]

for i in range(N):
    b = []
    A,B = map(int,input().split())
    c = []
    p,q = a[0]
    c.append((p,q))
    for j in range(len(a)-1):
        h,m = a[j+1]
        if h != p:
            c.append((h,m))
        p,q = h,m
    for h,m in c:
        if h-A >= 0:
            b.append((h-A,m))
        if m-B>= 0:
            b.append((h,m-B))
    if b == []:
        print(i)
        exit(0)
    a = set(b)
    a = list(a)
    a.sort()
    a.reverse()
print(N)