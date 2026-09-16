import sys
input = sys.stdin.readline

def dfs(depth , start , arr):
    if depth ==6:
        print(" ".join(map(str,arr)))
        return
    
    for s in range(start , k):
        arr.append(S[s])
        dfs(depth + 1 , s+1 , arr)
        arr.pop()
        
while True:
    data = list(map(int,input().split()))
    k = data[0]
    
    if k == 0:
        break
    S = data[1:]
    dfs(0,0,[])
    print()
    