import sys
input = sys.stdin.readline

n,k = map(int,input().split())
order = list(map(int,input().split()))

multitap = []
cnt = 0

for i in range(k):
    cur = order[i]
    if cur in multitap :
        continue
    
    if len(multitap) < n :
        multitap.append(cur)
        continue
    far = -1
    idx_remove = -1

    for idx , d in enumerate(multitap):
        if d not in order[i+1:]:
            idx_remove = idx
            break
        else:
            next_use = order[i+1:].index(d)
            if next_use > far :
                far = next_use
                idx_remove = idx
    multitap[idx_remove] = cur
    cnt += 1
print(cnt)