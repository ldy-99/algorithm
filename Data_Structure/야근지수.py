# 프로그래머스 야근지수 문제
# 그리디적 사고도 가능한 문제
# 최대힙과 최소힙은 헷갈리지 않는게 중요. 기본은 최소 힙 형태이다.
import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        w = -heapq.heappop(works)  # 가장 큰 작업량
        w -= 1                     # 작업량 1 감소
        heapq.heappush(works, -w)  # 다시 힙에 삽입

    return sum(w ** 2 for w in works)