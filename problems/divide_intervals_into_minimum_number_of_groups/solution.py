class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        A = []
        
        for a, b in intervals:
            A.append([a, 1])
            A.append([b+1, -1])
        
        res = curr = 0
        print(sorted(A))
        for a, diff in sorted(A):
            curr += diff
            res = max(res, curr)
        return res