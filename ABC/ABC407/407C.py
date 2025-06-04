S = list(input())
cnt = 0
l = len(S)
while S != []:
    x = S.pop()
    a = (int(x)-cnt)%10
    cnt += a
print(cnt+l)
