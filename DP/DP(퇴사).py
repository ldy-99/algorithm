import sys
input = sys.stdin.readline

N = int(input())  
a = [list(map(int,input().split())) for _ in range(N)] 
dp = [0] * (N+1)

for i in range(N):
    t,p = a[i]
    dp[i+1] = max(dp[i+1] , dp[i])
    
    if i + t <= N:
        dp[i+t] = max(dp[i+t] , dp[i] + p)
print(dp[N])