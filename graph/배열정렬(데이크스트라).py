import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq

def dijk(N,M,state,target,op):
    INF = float('inf')
    pq = [(0,state)]
    dist = {state : 0}
    
    while pq:
        curdist,curstate = heapq.heappop(pq)
        if curdist > dist.get(curstate,INF): 
            continue
        if curstate == target :
            return curdist

        for L,R,C in op:
            new_list = list(curstate)
            new_list[L-1],new_list[R-1] = new_list[R-1] , new_list[L-1]
            new_state = tuple(new_list)
            new_dist = curdist + C
            if new_dist < dist.get(new_state,INF):
                dist[new_state] = new_dist
                heapq.heappush(pq, (new_dist,new_state))
    return -1

N=int(input())
state=tuple(map(int,input().split()))
target=tuple(sorted(list(state)))
M=int(input())
op = [list(map(int,input().split())) for _ in range(M)]
print(dijk(N,M,state,target,op))