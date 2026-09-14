import sys

def solve(hist):
    stack = []
    maxarea = 0
    idx = 0
    n = len(hist)
    
    while idx < n :
        if not stack or hist[stack[-1]] <= hist[idx] :
            stack.append(idx)
            idx += 1
        else:
            top = stack.pop()
            width = idx if not stack else idx - stack[-1] - 1
            area = hist[top] * width
            maxarea = max(maxarea , area)
            
    while stack:
        top = stack.pop()
        width = idx if not stack else idx - stack[-1]-1
        area = hist[top] * width
        maxarea = max(maxarea , area)
        
    return maxarea

for line in sys.stdin:
    nums = list(map(int,line.split()))
    if nums[0] == 0:
        break
    print(solve(nums[1:]))