n = int(input())
p = [0] + list(map(int, input().split()))

visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1

        cur = i

        while not visited[cur]:
            visited[cur] = True
            cur = p[cur]

print(count)

# p = [3, 2, 7, 8, 1, 4, 5, 6] 일 때 , 

# 1 → 3 → 7 → 5
# ↑             ↓
# └─────────────┘

# 2 ──┐
# ↑   │
# └───┘

# 4 → 8 → 6
# ↑       ↓
# └───────┘