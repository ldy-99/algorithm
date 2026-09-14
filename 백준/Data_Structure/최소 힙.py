import heapq
import sys

input = sys.stdin.readline  

def solution(N):
    min_heap = []
    results = []

    for _ in range(N):
        x = int(input().strip())
        if x == 0:
            if not min_heap:
                results.append(0)
            else:
                results.append(heapq.heappop(min_heap))
        else:
            heapq.heappush(min_heap, x)
    
    return results

N = int(input().strip())  # 연산 개수 입력
res = solution(N)  # 연산 처리
print("\n".join(map(str, res)))  # 결과 출력