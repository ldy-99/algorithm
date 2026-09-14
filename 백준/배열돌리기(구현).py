import sys
input = sys.stdin.readline
from collections import deque

def rotate(l,r):
    d = deque(l)
    d.rotate(-r)
    return list(d)

def extract(arr,n,m):
    layers= []
    cnt = min(n,m) // 2
    for lay in range(cnt):
        ex = []
        for j in range(lay, m-lay):
            ex.append(arr[lay][j])
            
        for i in range(lay+1 , n-lay):
            ex.append(arr[i][m-1-lay])
            
        for j in range(m-2-lay , lay-1, -1):
            ex.append(arr[n-1-lay][j])
            
        for i in range(n-2-lay, lay, -1):
            ex.append(arr[i][lay])
        layers.append(ex)
    return layers

def insert(arr,layers,n,m):
    cnt = min(n,m) // 2
    for lay in range(cnt):
        idx = 0
        
        for j in range(lay, m - lay):
            arr[lay][j] = layers[lay][idx]
            idx +=1
        for i in range(lay+1, n-lay):
            arr[i][m-1-lay] = layers[lay][idx]
            idx +=1
        for j in range(m-2-lay , lay-1 , -1):
            arr[n-lay-1][j] = layers[lay][idx]
            idx +=1
        for i in range(n-2-lay , lay , -1):
            arr[i][lay] = layers[lay][idx]
            idx +=1

def sol(arr,n,m,r):
    layers = extract(arr,n,m)
    for i in range(len(layers)):
        layers[i] = rotate(layers[i] , r)
    
    insert(arr,layers,n,m)
    return arr
            
n,m,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
result = sol(arr,n,m,r)

for row in result:
    print(*row)