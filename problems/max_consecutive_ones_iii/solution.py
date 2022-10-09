class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        s=0
        
        for e in range(0, len(nums)):
            
            if nums[e]==0:
                k-=1
            
            if k<0:
                
                if nums[s]==0:
                    k+=1
                s+=1
        
        return e-s+1