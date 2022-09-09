class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        obj = dict()
        
        for v in nums:
            if v not in obj:
                obj[v] = 1
            else:
                return v