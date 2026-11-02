from collections import defaultdict
def solution(info, edges):
    answer = 0
    graph = defaultdict(list)
    
    for parent,child in edges :
        graph[parent].append(child)
    
    def dfs(sheep,wolf, arr):
        nonlocal answer
        
        # 여기서 부터 중요. 후보자 리스트의 역할
        for node in arr :
            nxt_sheep = sheep + (info[node] == 0)
            nxt_wolf = wolf + (info[node] == 1)
            
            # 가지치기 조건 늑대의 수가 양과 많거나 같아짐
            if nxt_wolf >= nxt_sheep :
                continue
            
            answer = max(answer , nxt_sheep)
            nxt_arr = arr[:]
            # 현재 방문한 노드 제거와 새로 방문 가능해진 자식 추가
            nxt_arr.remove(node)
            nxt_arr.extend(graph[node])
            dfs(nxt_sheep , nxt_wolf , nxt_arr)

    dfs(0,0,[0])
    return answer