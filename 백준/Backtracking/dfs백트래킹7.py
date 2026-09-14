import sys
input = sys.stdin.readline

N = int(input())
W = list(map(int,input().split()))

# x번째 제거 ,  w[x-1] * w[x+1] 값들의 최대를 구하라.
# 제거 한 후에는 N 감소 후 재배치
e = 0

def dfs(start , w ):
    global e
    if len(w) == 2:
        e = max(e , start)
        return
    
    for i in range(1, len(w)-1):
        g = w[i-1] * w[i+1]
        new_ = w[:i] + w[i+1:]
        dfs(start + g , new_ )

dfs(0,W)
print(e)