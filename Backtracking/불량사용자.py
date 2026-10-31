#프로그래머스 불량 사용자
#백트래킹 , 순열 , 집합
#문자열 매칭 비교가 핵심
from itertools import permutations as p

def match(user, banned):
    if len(user) != len(banned):
        return False

    for a, b in zip(user, banned):
        if b == '*':
            continue

        if a != b:
            return False

    return True

def solution(user_id, banned_id):
    results = set()

    for user in p(user_id, len(banned_id)):
        valid = True

        for i in range(len(banned_id)):
            if not match(user[i], banned_id[i]):
                valid = False
                break

        if valid:
            results.add(frozenset(user))

    return len(results)