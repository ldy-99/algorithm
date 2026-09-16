import sys
input = sys.stdin.readline

def dfs(depth, ans):
    if depth == M:
        print(*ans)
        return
    
    for n in nums:
        if n not in  ans:
             ans.append(n)
             dfs(depth+1 , ans)
             ans.pop()
    
N,M = map(int,input().split())
nums = sorted(map(int,input().split()))
dfs(0,[])

# N개의 자연수와 자연수 M이 주어졌을 때,
#아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램