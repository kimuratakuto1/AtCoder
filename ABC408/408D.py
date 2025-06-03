t = int(input())
INF = float('inf')
for _ in range(t):
    n = int(input())
    s = input()
    dp = [[INF]*3 for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        if s[i]=='0':
            dp[i+1][0]=min(dp[i+1][0],dp[i][0])
            dp[i+1][1]=min(dp[i+1][1],dp[i][0]+1,dp[i][1]+1)
            dp[i+1][2]=min(dp[i+1][2],dp[i][1],dp[i][2])
        else:
            dp[i+1][0]=min(dp[i+1][0],dp[i][0]+1)
            dp[i+1][1]=min(dp[i+1][1],dp[i][0],dp[i][1])
            dp[i+1][2]=min(dp[i+1][2],dp[i][1]+1,dp[i][2]+1)
    print(min(dp[n]))
t=int(input())
INF=float('inf')
for _ in range(t):
    n=int(input())
    s=input()
    dp=[[INF]*3 for _ in range(n+1)]
    dp[0][0]=0
    for i in range(n):
        if s[i]=='0':
            dp[i+1][0]=min(dp[i+1][0],dp[i][0])
            dp[i+1][1]=min(dp[i+1][1],dp[i][0]+1,dp[i][1]+1)
            dp[i+1][2]=min(dp[i+1][2],dp[i][1],dp[i][2])
        else:
            dp[i+1][0]=min(dp[i+1][0],dp[i][0]+1)
            dp[i+1][1]=min(dp[i+1][1],dp[i][0],dp[i][1])
            dp[i+1][2]=min(dp[i+1][2],dp[i][1]+1,dp[i][2]+1)
    print(min(dp[n]))