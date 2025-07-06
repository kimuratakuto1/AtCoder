T = int(input())
ans = []
for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    B = []
    if N == 2:
        ans.append("Yes")
    else:
        for j in range(N):
            B.append(abs(A[j]))
        B.sort()
        flag = True
        for j in range(N-2):
            if B[j+2]*B[j] != B[j+1]**2:
                flag = False
        if flag == False:
            ans.append("No")
        else:
            C = []
            D = []
            E = []
            for j in range(N):
                C.append(-B[j])
                if j % 2 == 0:
                    D.append(B[j])
                    E.append(-B[j])
                else:
                    E.append(B[j])
                    D.append(-B[j])
            C.sort()
            D.sort()
            E.sort()
            if A == B or A == C or A == D or A == E:
                ans.append("Yes")
            else:
                ans.append("No")
for i in range(T):
    print(ans[i])

