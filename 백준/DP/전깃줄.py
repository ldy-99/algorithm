import sys
input = sys.stdin.readline
T = int(input())
wires = [tuple(map(int,input().split())) for _ in range(T)]
wires.sort() # A 전봇대 기준으로 정렬하면 B에서 LIS 길이를 구하면 됨.
B = [b for _,b in wires]
dp = [1] * T
for i in range(T):
    for j in range(i):
        if B[i] > B[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(T - max(dp))      