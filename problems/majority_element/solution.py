class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        obj = dict()
        
        for v in nums:
            obj[v] = obj.get(v, 0) + 1
            
            if obj[v] > len(nums)//2:
                return v
        
        