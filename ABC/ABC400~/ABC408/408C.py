N,M = map(int,input().split())
UD = [0 for i in range(N+2)]

for i in range(M):
    L,R = map(int,input().split())
    UD[L] += 1
    UD[R+1] -= 1

check = 0
ans = 10**10
for i in range(1,N+1):
    check += UD[i]
    if ans > check:
        ans = check
print(ans)