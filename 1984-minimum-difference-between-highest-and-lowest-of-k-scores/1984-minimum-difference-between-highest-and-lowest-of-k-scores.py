class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        
        nums.sort()
        mini=float(inf)
    
        
        for e in range(k-1, len(nums)):
            mini = min(mini, nums[e]-nums[e-k+1])
        
        return mini