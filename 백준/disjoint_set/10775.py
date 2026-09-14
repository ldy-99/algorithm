import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        # 실수 포인트
        parent[a] = b

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
cnt = 0
for _ in range(P):
    gi = int(input())
    t = find(gi)
    if t == 0:
        break
    elif t > 0 :
        union(t,t-1)
        cnt += 1
print(cnt)

## 분리집합을 사용하는 것을 바로 떠올리기 어려울 수 있다.
## union(t,t-1) 을 하는 이유는 t를 선점하게 되면 t는 사용할 수 없으므로,
## t-1에 도킹하도록 안내하는게 최선책이다.
## 단순 반복문은 시간초과 발생