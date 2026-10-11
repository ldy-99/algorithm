#백준 케빈 베이컨

import sys
input = sys.stdin.readline
from collections import deque,defaultdict

n,m=map(int,input().split())
graph = defaultdict(list)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    q = deque([start])
    
    while q:
         curr = q.popleft()
         for next in graph[curr]:
             if visited[next] == -1:
                 visited[next] = visited[curr] + 1
                 q.append(next)
    return sum(visited[1:])

mins = float('inf')
ans = 0
for i in range(1,n+1):
    tt = bfs(i)
    if tt < mins:
        mins = tt
        ans = i
print(ans)