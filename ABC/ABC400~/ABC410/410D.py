from collections import deque
N,M = map(int,input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    A,B,W = map(int,input().split())
    G[A].append((B,W))


can = [[False]*1024 for _ in range(N+1)]
can[1][0] = True

Q = deque()
Q.append((1,0))
while Q:
    v,W = Q.popleft()
    for x,Y in G[v]:
        if can[x][W^Y] == False:
            can[x][W^Y] = True
            Q.append((x,W^Y))


for i in range(1024):
    if can[N][i] == True:
        print(i)
        exit(0)
print(-1)