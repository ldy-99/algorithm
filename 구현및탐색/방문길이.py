# 프로그래머스 방문 길이
def isvalid(x,y):
    return 0 <= x <= 10 and 0 <= y <= 10

def solution(dirs):
    answer = 0
    visited = set()
    start = (5,5)
    
    for d in dirs :
        x,y = start
        if d == 'U' :
            x -= 1
        elif d == 'D' :
            x += 1
        elif d == 'L' :
            y -= 1
        elif d == 'R' :
            y += 1
        
        if not isvalid(x,y):
            continue
        end = (x,y)
        path = tuple(sorted((start,end)))
        visited.add(path)
        
        start = end # 좌표 갱신
    return len(visited)