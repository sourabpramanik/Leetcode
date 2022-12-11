class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        last=-1
        for i, n in enumerate(nums):
            if n==target:
                if first==-1:
                    first=i
                if first!=-1:
                    last=i
        
        return [first, last]