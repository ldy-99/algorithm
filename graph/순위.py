# 프로그래머스 순위
# 순위 문제는 선수 간의 직접적인 경기 결과를 이용해 
# 간접적인 승패 관계까지 파악해야 하는 그래프 도달 가능성 문제입니다.

from collections import deque,defaultdict
def solution(n, results):
    answer = 0
    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)
    
    for a,b in results:
        win_graph[a].append(b)
        lose_graph[b].append(a)
    
    def bfs(start,graph):
        size = 0
        visited = set()
        q = deque()
        
        q.append(start)
        visited.add(start)
        
        while q :
            node = q.popleft()
            for nxt in graph[node]:
                if nxt not in visited :
                    visited.add(nxt)
                    q.append(nxt)
                    size += 1
        return size
    for i in range(1,n+1):
        size = bfs(i,win_graph) + bfs(i,lose_graph)
        if size == n-1 :
            answer += 1
    return answer