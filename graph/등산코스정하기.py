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

# 다익스트라 탐색 과정에서 현재 노드가 산봉우리인지, 다음 노드가 출입구인지 반복적으로 확인해야 합니다.
# 리스트를 사용하면 원소의 존재 여부를 확인하는 데 O(N)의 시간이 필요하지만, set은 해시 테이블을 기반으로 평균 O(1)에 확인할 수 있습니다.
# 따라서 반복적인 탐색 비용을 줄이기 위해 set으로 변환했습니다.