import sys
from collections import defaultdict
input = sys.stdin.readline

N,M = map(int,input().split())
friend = defaultdict(list)
visited = set()
state = False

for i in range(M):
    a , b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

def dfs(node,depth):
    global state
    visited.add(node)
    if depth == 5:
        state = True
        return
    
    for next in friend[node]:
        if next not in visited:
            dfs(next , depth+1)
    visited.remove(node)

for i in range(N):
    dfs(i,1)
    if state:
        break

if state:
    print(1)
else:
    print(0)