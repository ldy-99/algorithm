## ACM CRAFT
import sys
from collections import defaultdict , deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    graph=defaultdict(list)
    
    N,K = map(int,input().split())
    time = [0] + list(map(int,input().split()))
    edges = tuple(map(int,input().split()) for _ in range(K))
    
    indegree = [0] * (N+1)
    dp = [0] * (N+1)
    
    for a,b in edges:
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())
    
    q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0 :
            q.append(i)
            dp[i] = time[i]
    while q:
        node = q.popleft()
        for i in graph[node] :
            dp[i] = max(dp[i] , dp[node] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0 :
                q.append(i)
    print(dp[w])