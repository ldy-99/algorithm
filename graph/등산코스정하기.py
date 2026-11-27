# 프로그래머스 등산코스정하기
# 일반적인 최단거리의 다익스트라가 아님

from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    answer = []
    INF = float('inf')
    graph = defaultdict(list)

    # 리스트보다 set 이 in 연산에서 유리함
    gate_set = set(gates)
    summit_set = set(summits)

    # 그래프 모델링
    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijk():
        intensity = [INF] * (n + 1)
        pq = []

        # 모든 출입구를 시작점으로 설정 (중요)
        for gate in gates:
            intensity[gate] = 0
            heapq.heappush(pq, (0, gate))

        while pq:
            cur, node = heapq.heappop(pq)

            # 이미 더 좋은 경로를 발견한 경우
            if cur > intensity[node]:
                continue

            # 산봉우리에서는 추가 탐색하지 않음
            if node in summit_set:
                continue

            for nxt, weight in graph[node]:

                # 다른 출입구 방문 금지
                if nxt in gate_set:
                    continue

                new_intensity = max(cur, weight)

                if new_intensity < intensity[nxt]:
                    intensity[nxt] = new_intensity
                    heapq.heappush(pq, (new_intensity, nxt))

        return intensity

    intensity = dijk()
    for s in summits :
        answer.append((s,intensity[s]))
    answer.sort(key=lambda x : (x[1],x[0]))
    return answer[0]