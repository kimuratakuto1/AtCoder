N = int(input())
A = list(map(int,input().split()))

A = sorted(A)
ans = []
now = A[0]
ans.append(now)
for i in range(N-1):
    if now != A[i+1]:
        ans.append(A[i+1])
        now = A[i+1]
print(len(ans))
print(*ans)