from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    P, C, W = map(int, input().split())
    graph[P].append((C, W))
    graph[C].append((P, W))

def dfs(start, weight):
    for next, nextdist in graph[start]:
        if visited[next] == -1: 
            visited[next] = weight + nextdist
            dfs(next, visited[next])  

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)
end = visited.index(max(visited)) 

visited = [-1] * (n+1)
visited[end] = 0
dfs(end, 0)

print(max(visited))