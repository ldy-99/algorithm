import sys
input = sys.stdin.readline

def find(p,x):
    if p[x] == x:
        return x    
    p[x] = find(p,p[x])
    return p[x]

def union(p,r,x,y):
    xroot = find(p,x)
    yroot= find(p,y)
    
    if r[xroot] < r[yroot]:
        p[xroot] = yroot
        
    elif r[xroot]> r[yroot]:
        p[yroot] = xroot
    else:
        p[yroot] = xroot
        r[xroot] += 1

n, m = map(int, input().split())
p = [i for i in range(n+1)]
r = [0] *(n+1)

true = list(map(int,input().split()))
cnt = true[0]
true_people = true[1:] if cnt > 0 else []

# 진실 집합 
for person in true_people:
    p[person] = 0

parties = []
for _ in range(m):
    party = list(map(int,input().split()))
    party_size = party[0]
    party_people = party[1:]
    parties.append(party_people)
    for i in range(1,party_size):
        union(p,r,party_people[i-1],party_people[i])

lie = 0
for i in parties:
    if all(find(p,person) != find(p,0) for person in i):
        lie +=1
        # 모든 사람이 진실을 모르는 그룹에 속해있다면 거짓말이 가능 
print(lie)