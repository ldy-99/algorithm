import sys
input = sys.stdin.readline
from collections import deque

def D(n):
    return  (2*n) % 10000

def S(n):
    return 9999 if n== 0 else n-1

def L(n):
    s = str(n).zfill(4)
    return int(s[1:] + s[0])

def R(n):
    s = str(n).zfill(4)
    return int(s[-1] + s[:-1])

def bfs(A,B):   
    q = deque([(A, '')])
    visited = set()
    visited.add(A)
    
    while q:
        n , command = q.popleft()
        if n == B:
            return command
        
        for i,j in [(D(n),'D'),(S(n),'S'),(L(n),'L'),(R(n),'R')]:
            if i not in visited:
                visited.add(i)
                q.append((i,command + j))

T = int(input())
for _ in range(T):
    A,B=map(int,input().split())
    print(bfs(A,B))