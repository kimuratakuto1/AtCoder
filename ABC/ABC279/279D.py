A,B = map(int,input().split())
l = 0
r = 10**18
def f(x):
    return B*x + A/(1+x)**0.5
while (l+3 <= r):
    c1 = (l*2+r)//3
    c2 = (l+r*2)//3
    if f(c1) < f(c2):
        r = c2
    else:
        l = c1
ans = min(f(l),f(l+1),f(r))
print(ans)


