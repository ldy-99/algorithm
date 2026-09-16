import sys
input =sys.stdin.readline

N,M,K = map(int,input().split())
candy =[0] + list(map(int,input().split()))

def find(p,x):
    if p[x] == x:
        return x
    p[x] = find(p,p[x])
    return p[x]

def union(a, b):
    a, b = find(p,a), find(p,b)
    if a != b:
        p[b] = a

p = [i for i in range(N+1)]

for _ in range(M):
    a,b= map(int,input().split())
    union(a,b)

group = {}
size = {}

for i in range(1,N+1) :
    root = find(p,i)
    group[root] = group.get(root,0) + candy[i]
    size[root] = size.get(root,0) + 1

dp = [0] * K
for root in group :
    w = size[root]
    v = group[root]
    for i in range(K-1,w-1 , -1) :
        dp[i] = max(dp[i] , dp[i-w] + v)
print(max(dp))
print(dp)
print(group)
print(size)