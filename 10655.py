import sys
input = sys.stdin.readline

def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

N = int(input())
check = []

for i in range(N):
    s,e = map(int,input().split())
    check.append((s,e))

dist = 0
for i in range(N-1):
    dist += get_dist(check[i],check[i+1])

ans = 0
for i in range(1,N-1):
    original = get_dist(check[i-1], check[i]) + get_dist(check[i], check[i+1])
    skip = get_dist(check[i-1], check[i+1])

    saved = original - skip
    ans = max(ans , saved)
print(dist-ans)