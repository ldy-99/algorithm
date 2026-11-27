# 프로그래머스 순위 검색(해시,이분탐색)

from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    db = defaultdict(list)
    for i in info :
        tokens = i.split()
        user_info = tokens[:-1]
        score = int(tokens[-1])
        
        def dfs(idx, cur):
            if idx == 4:
                db[cur].append(score)
                return
            # 두 가지 선택지 (dfs)
            dfs(idx + 1 , cur + user_info[idx])
            dfs(idx + 1 , cur + '-')
        dfs(0,'')
        
    for key in db.keys():
        db[key].sort()
        
    for q in query:
        q_tokens = [x for x in q.split() if x!= 'and']
        q_key = ''.join(q_tokens[:-1])
        q_score = int(q_tokens[-1])
            
        if q_key in db :
            scores = db[q_key]
            idx = bisect_left(scores , q_score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
    return answer
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
result = solution(info,query)
print(result)

#  product를 사용하는 방법
# options = [(x, '-') for x in user_info]  -> x 거나 - 이거나
# for case in product(*options):
#     db[case].append(score)

# DFS
# → 각 속성을 유지할지 변경할지 재귀적으로 선택한다.

# product
# → 각 속성에서 가능한 선택지를 모두 조합한다.

# combinations
# → 변경할 속성의 위치를 선택한다.

# 비트마스킹
# → 각 속성의 선택 상태를 비트로 표현한다.