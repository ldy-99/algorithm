import sys
import heapq
input = sys.stdin.readline

def sol(op):
    min_heap=[]
    max_heap=[]
    sync= {}   # 힙 동기화
    for o in op:
        if o[0] == 'I':
            num = int(o[1])
            heapq.heappush(min_heap,num)
            heapq.heappush(max_heap, - num)
            sync[num] = sync.get(num,0) + 1  # sync에 num이 존재하면 해당 값을 가져온다. 존재하지않으면 0을 반환
        elif o[0] == 'D':
            if not sync:
                continue
            if o[1] == '1':   # max
                while max_heap:
                    ismax = -heapq.heappop(max_heap)
                    if sync.get(ismax,0) >0:  #유효값인지 확인
                        sync[ismax] -= 1
                        if sync.get(ismax) == 0:
                            del sync[ismax]
                        break
            elif o[1] == '-1':  # min
                while min_heap:
                    ismin = heapq.heappop(min_heap)
                    if sync.get(ismin,0) > 0:
                        sync[ismin] -= 1
                        if sync.get(ismin) == 0:
                            del sync[ismin]
                        break
    if not sync:
        return "EMPTY"
    
    while max_heap:
        ismax = -heapq.heappop(max_heap)
        if sync.get(ismax,0) > 0:
            break
    while min_heap:
        ismin = heapq.heappop(min_heap)
        if sync.get(ismin,0)>0:
            break
    return f"{ismax} {ismin}"            
T= int(input().strip())
for _ in range(T):
    k = int(input().strip())
    op = [input().strip().split() for _ in range(k)]
    print(sol(op))
    

# 다른 풀이 방식(프로그래머스)
# 이 문제는 최소 힙과 최대 힙을 동시에 사용하면서 발생하는 동기화 문제에대한 생각을 해볼 수 있는 문제이다.

import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    # 실제 삭제가 아닌 삭제를 표기하기 위한 리스트
    deleted = [False] * len(operations)

    for i, op in enumerate(operations):
        command, num = op.split()
        num = int(num)

        if command == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))

        elif command == 'D':
            if num == -1:
                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    value, idx = heapq.heappop(min_heap)
                    deleted[idx] = True # 논리적 삭제 (반대쪽 힙에는 남아있을 수 있기 때문)

            else:
                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    value, idx = heapq.heappop(max_heap)
                    deleted[idx] = True # 논리적 삭제(반대쪽 힙에는 남아있을 수 있기 때문)

# 중요) 무효한 숫자들을 힙에서 제거하기위해 while문을 for문 밖에서도 실행 (지연정리)
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)

    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap:  # min_heap or max_heap
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]