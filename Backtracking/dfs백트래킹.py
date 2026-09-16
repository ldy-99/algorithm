import sys
input = sys.stdin.readline

def dfs(depth,ans):
    global maxv,minv
    
    if depth == N-1:
        maxv = max(maxv,ans)
        minv = min(minv,ans)
        return
    
    for i in range(4):
        if op[i] > 0 :
            op[i] -=1
            if i==0:
                dfs(depth+1 , ans + A[depth+1])
            elif i==1:
                dfs(depth+1 , ans - A[depth+1])
            elif i==2:
                dfs(depth+1 , ans * A[depth+1])
            elif i==3:
                if ans < 0:
                    dfs(depth+1 , -(abs(ans) // A[depth+1]))
                else:
                    dfs(depth+1 , ans // A[depth+1])
            op[i] += 1

N=int(input())
A=list(map(int,input().split()))
op = list(map(int,input().split()))
maxv= -float('inf')
minv= float('inf')
dfs(0 , A[0])

print(maxv)
print(minv)