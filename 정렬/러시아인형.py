# 354. Russian Doll Envelopes (leetcode)
# 인사고과 문제에서 한단계 더 나아간 문제
# 2차원을 1차원으로 축소하는 사고
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        # 정렬을 통해 비교 조건을 줄임(너비 비교 조건 제거)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        lis = []

        for w, h in envelopes:
            idx = bisect_left(lis, h)

            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h

        return len(lis)
S1 = Solution()
print(S1.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))