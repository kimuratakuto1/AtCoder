from collections import deque

Q = int(input())
A = deque()
ANS = []
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        c,x = query[1],query[2]
        A.append([c,x]) #xをc個追加
    else:
        k = query[1]
        kflag = False
        ans = 0
        while kflag == False:
            p = A.popleft()
            c,x = p[0],p[1]
            if k <= c:
                A.appendleft([c-k,x])
                ans += k*x
                kflag = True
            else:
                k -= c
                ans += c*x
        ANS.append(ans)

for a in ANS:
    print(a)