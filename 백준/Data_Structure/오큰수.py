import sys
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

stack = []
ans = [-1] * N

for i in range(N):
    while stack and A[stack[-1]] < A[i] :
        index = stack.pop()
        ans[index] = A[i]
    stack.append(i)

print(*ans)