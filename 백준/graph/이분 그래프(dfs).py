import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph,v, C , visited):
    visited[v] = C
    
    for next in graph[v]:
        if visited[next] == -1:
            if not dfs(graph,next, 1- C , visited):
                return False
        elif visited[next] == visited[v]:
            return False
    return True

def solution(V,E,edges):
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [-1] * (V+1)
    
    for node in range(1,V+1):
        if visited[node] == -1:
            if not dfs(graph,node,0, visited):
                return "NO"
    return "YES"

K=int(input().strip())
ans = []
for _ in range(K):
    V , E = map(int,input().split())
    edges = [tuple(map(int,input().split())) for _ in range(E)]
    ans.append(solution(V,E,edges))
print("\n".join(ans))