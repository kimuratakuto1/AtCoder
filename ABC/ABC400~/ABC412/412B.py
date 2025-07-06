S = input()
T = input()

flag = False
ans = True
for i in range(len(S)):
    if S[i].isupper() and flag == False:
        flag = True

    elif S[i].isupper() and flag == True:
        check = S[i-1]
        checkflag = False

        for j in range(len(T)):
            if check == T[j]:
                checkflag = True
        if checkflag == False:
            print("No")
            exit(0)
print("Yes")
