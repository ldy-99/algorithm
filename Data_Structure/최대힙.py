import heapq
import sys

input = sys.stdin.readline  

def solution(N):
    max_heap = []
    results = []

    for _ in range(N):
        x = int(input().strip())
        if x == 0:
            if not max_heap:
                results.append(0)
            else:
                # 힙에서 최댓값을 꺼내고, 음수를 다시 양수로 변환
                results.append(-heapq.heappop(max_heap))
        else:
            # 최대 힙 구현을 위해 음수로 변환하여 삽입
            heapq.heappush(max_heap, -x)
    
    return results
N = int(input().strip())  
res = solution(N) 
print("\n".join(map(str, res)))  