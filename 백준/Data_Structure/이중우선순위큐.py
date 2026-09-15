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