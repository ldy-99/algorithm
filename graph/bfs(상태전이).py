import sys
from collections import deque
input = sys.stdin.readline
def bfs(A,B):
    visited = set()
    q = deque([(A,0)])  # 연산 횟수 추적
    while q:
        num,cnt = q.popleft()
        if num == B:
            return cnt +1
        if num in visited:
            continue
        visited.add(num)
        if num*2 <= B:
            q.append((num*2 , cnt+1))
        if num * 10 + 1 <=B:
            q.append((num*10+1 , cnt+1))
    return -1
A,B = map(int,input().split())
print(bfs(A,B))