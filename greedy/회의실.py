import sys
input = sys.stdin.readline

def sol(M):
    M.sort(key=lambda x: (x[1],x[0]))
    cnt=0
    last=0
    
    for start,end in M:
        if start >= last:
            cnt+=1
            last=end
    return cnt
n=int(input().strip())
M=[tuple(map(int,input().split())) for _ in range(n)]
print(sol(M))