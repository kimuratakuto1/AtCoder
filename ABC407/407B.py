X,Y = map(int,input().split())
count = 0
def Xcheck(a,b):
    if a+b >= X:
        return True
    else:
        return False

def Ycheck(a,b):
    if abs(a-b) >= Y:
        return True
    else:
        return False
    
for i in range(1,7):
    for j in range(1,7):
        if Xcheck(i,j) or Ycheck(i,j):
            count += 1
print(count/36)