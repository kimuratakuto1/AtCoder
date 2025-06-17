N,Q = map(int,input().split())
A = [i for i in range(1,N+1)]

cnt = 0
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        A[(query[1]+cnt-1)%N] = query[2]
    elif query[0] == 2:
        print(A[(query[1]+cnt-1)%N])
    else:
        cnt += query[1]
