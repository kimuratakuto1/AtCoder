A,B = map(int,input().split())
x = A//B
y = A/B
if y-x>=0.5:
    print(x+1)
else:
    print(x)