class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        minCount=float(inf)
        currSum=0
        
        for e in range(0, len(nums)):
            currSum+=nums[e]
            
            while currSum >= target:
                minCount = min(minCount, e-s+1)
                currSum-=nums[s]
                s+=1
        
        return 0 if minCount==float(inf) else minCount