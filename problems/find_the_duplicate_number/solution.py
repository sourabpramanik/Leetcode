class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = Counter(nums)
        for k in m:
            if m[k]>1:
                return k
        return -1