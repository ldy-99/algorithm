# 백준 웜홀 -- 벨만포드 (음수 사이클 탐지)

import sys
input = sys.stdin.readline
inf = float('inf')

def bellman(n,graph):
    dist = [0] * (n+1)
    
    for _ in range(n-1):
        for u,v,w in graph :
            if dist[v] > dist[u] + w :
                dist[v] = dist[u] + w

    for u,v,w in graph :
        if dist[v] > dist[u] + w :
            return True
    return False

def main():
    tc = int(input())
    ans = []
    for _ in range(tc):
        N,M,W = map(int,input().split())
        graph = []
        
        for _ in range(M):
            S,E,T = map(int,input().split())
            graph.append((S,E,T))
            graph.append((E,S,T))
        
        for _ in range(W):
            S,E,T = map(int,input().split())
            graph.append((S,E,-T))
        
        ans.append(("YES" if bellman(N,graph) else "NO"))
    print('\n'.join(ans))
main()