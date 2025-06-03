N,S = map(int,input().split())
T = list(map(int,input().split()))
if T[0] > S:
    print("No")
    exit(0)
for i in range(N-1):
    if T[i+1] - T[i] > S:
        print("No")
        exit(0)
print("Yes")