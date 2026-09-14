import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, graph, ages, who):
    q = deque([start])
    visited = {start}

    found = False
    min_age = 316
    while q:
        curr = q.popleft()
        for nxt in graph[curr]:
            if nxt not in visited:
                visited.add(nxt)
                found = True
                min_age = min(min_age, ages[who[nxt]])
                q.append(nxt)

    return min_age if found else "*"

def solution():
    while True:
        line = input().split()
        if not line:
            break
        N, M, I = map(int, line)
        ages = [0] + list(map(int, input().split()))
        graph = [[] for _ in range(N + 1)]
        for _ in range(M):
            u, v = map(int, input().split())
            graph[v].append(u)

        # pos[x]: n
        # who[n]: x
        pos = list(range(N + 1))
        who = list(range(N + 1))

        for _ in range(I):
            cmd = input().split()

            if cmd[0] == 'T':
                a, b = map(int, cmd[1:])
                na, nb = pos[a], pos[b]
                pos[a], pos[b] = nb, na
                who[na], who[nb] = b, a
            else:
                e = int(cmd[1])
                start_node = pos[e]
                result = bfs(start_node, graph, ages, who)
                print(result)
solution()