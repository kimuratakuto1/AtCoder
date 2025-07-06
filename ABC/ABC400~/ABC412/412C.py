from collections import deque
T = int(input())
ans = []
for i in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    first = S[0]
    last = S[N-1]
    S.sort()
    d = {}
    cnt = 1
    for j in range(N):
        if S[j] < first:
            continue
        elif first == S[j]:
            d[cnt] = S[j]
        elif last == S[j]:
            if 
        elif S[j] <= d[cnt] * 2:
            d[cnt+1] = S[j]
        else:
            cnt += 1

        if last == S[j]:

    print(d)
    if cnt == 1:
        ans.appned(-1)
    else:
        ans.append(cnt)
print(ans)

        
        


