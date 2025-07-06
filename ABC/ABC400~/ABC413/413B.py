N = int(input())
L = set()
S = []
for i in range(N):
    s = input()
    S.append(s)
for i in range(0,N-1):
    for j in range(i+1,N):
        L.add(S[i]+S[j])
        L.add(S[j]+S[i])

print(len(L))