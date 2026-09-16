#프로그래머스 바이러스파이프

from collections import deque

def solution(n, infection, edges, k):
    graph = [[] for _ in range(n + 1)]

    for a, b, pipe_type in edges:
        graph[a].append((b, pipe_type))
        graph[b].append((a, pipe_type))

    def spread(infected, pipe_type):
        infected = set(infected)
        queue = deque(infected)

        while queue:
            cur = queue.popleft()

            for nxt, nxt_type in graph[cur]:
                if nxt_type == pipe_type and nxt not in infected:
                    infected.add(nxt)
                    queue.append(nxt)

        return frozenset(infected)

    infected_states = {frozenset([infection])}

    for _ in range(k):
        next_states = set()

        for infected in infected_states:
            for pipe_type in range(1, 4):
                next_states.add(spread(infected, pipe_type))

        infected_states = next_states

    return max(map(len, infected_states))