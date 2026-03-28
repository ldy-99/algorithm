import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dicA = defaultdict(int)
dicB = defaultdict(int)

for a in A:
    dicA[a] += 1
for b in B:
    dicB[b] += 1

common = []
for k, v in dicA.items():
    if k in dicB:
        common_count = min(v, dicB[k])
        common.extend([k] * common_count)

cnt = len(common)
print(cnt)

## 쌍(cnt)을 찾는건 해시로 쉽게 가능하다 .
## 배열까지 출력해야 하므로 이 부분이 삽질할 수 있는 부분.

resA = list(common)
resB = list(common)

for k, v in dicA.items():
    diff = v - (min(v, dicB[k]) if k in dicB else 0)
    if diff > 0:
        resA.extend([k] * diff)

for k, v in dicB.items():
    diff = v - (min(v, dicA[k]) if k in dicA else 0)
    if diff > 0:
        resB.extend([k] * diff)

print(*(resA))
print(*(resB))