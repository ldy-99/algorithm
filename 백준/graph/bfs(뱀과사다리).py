import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
ladder = {x: y for x, y in [map(int, input().split()) for _ in range(N)]}
snake = {x: y for x, y in [map(int, input().split()) for _ in range(M)]}

def L(x):
    return ladder.get(x, x)  

def S(x):
    return snake.get(x, x)  

def D(x):
    return [x + i for i in range(1, 7) if x + i <= 100]  

def bfs(start,end):
    visited = set()
    q = deque([(start, 0)]) 
    visited.add(start)

    while q:
        cur, count = q.popleft()
        if cur == end:
            return count  

        for i in D(cur): 
            i = L(i)  
            i = S(i)  
            if i not in visited:
                visited.add(i)
                q.append((i, count + 1)) 
print(bfs(1,100))  