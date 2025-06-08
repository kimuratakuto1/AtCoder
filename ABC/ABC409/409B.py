N = int(input())
A = list(map(int,input().split()))

for i in range(N+1):
    cnt = 0
    for j in range(N):
        if N - i <= A[j]:
            cnt += 1
    if N - i <= cnt:
        print(N - i)
        exit(0)