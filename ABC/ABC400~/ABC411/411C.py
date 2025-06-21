N,Q = map(int,input().split())
A = list(map(int,input().split()))
dict = {i+1:False for i in range(N)}

cnt = 0
if N == 1:
    for i in range(Q):
        if i % 2 == 0:
            print(1)
        else:
            print(0)
else:
    for i in range(Q):
        #端を探索するときは注意
        if A[i] == 1:
            if dict[A[i]] == False:
                if dict[A[i]+1] == False:
                    cnt += 1
                else:
                    pass
                dict[A[i]] = True
            else:
                if dict[A[i]+1] == False:
                    cnt -= 1
                else:
                    pass
                dict[A[i]] = False
        elif A[i] == N:
            if dict[A[i]] == False:
                if dict[A[i]-1] == False:
                    cnt += 1
                else:
                    pass
                dict[A[i]] = True
            else:
                if dict[A[i]-1] == False:
                    cnt -= 1
                else:
                    pass
                dict[A[i]] = False
        else:
            if dict[A[i]] == False:
                if dict[A[i]-1] == dict[A[i]+1] == False:
                    cnt += 1
                elif dict[A[i]-1] == dict[A[i]+1] == True:
                    cnt -= 1
                else:
                    pass
                dict[A[i]] = True
            else:
                if dict[A[i]-1] == dict[A[i]+1] == False:
                    cnt -= 1
                elif dict[A[i]-1] == dict[A[i]+1] == True:
                    cnt += 1
                else:
                    pass
                dict[A[i]] = False
        print(cnt)
