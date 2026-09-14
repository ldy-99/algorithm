import sys
input = sys.stdin.readline

n = int(input())
heights = [int(input()) for _ in range(n)]

stack = []
ans = 0

for h in heights:
    while stack and stack[-1] <= h:
        stack.pop()
    ans += len(stack)
    stack.append(h)
print(ans)