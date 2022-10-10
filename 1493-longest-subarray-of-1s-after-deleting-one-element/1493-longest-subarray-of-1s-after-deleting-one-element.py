class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        s=0
        k=1
        for e in range(0, len(nums)):
            
            if nums[e]==0:
                k-=1
            
            if k<0:
                
                if nums[s]==0:
                    k+=1
                s+=1
        
        return e-s