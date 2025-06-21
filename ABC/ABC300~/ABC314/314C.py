N,M = map(int,input().split())
S = list(input())
C = list(map(int,input().split()))

dict = {i+1:[] for i in range(M)}

for i in range(N):
    dict[C[i]].append(S[i])
print(dict)

ans = []

#for i in range(N):
