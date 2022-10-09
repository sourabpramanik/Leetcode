class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        s=0
        odd=0
        nice=0
        ans=0
        
        for e in range(0, len(nums)):
            
            if nums[e]%2:
                odd+=nums[e]%2
                nice=0
            while odd==k:
                odd-=nums[s]%2
                nice+=1
                s+=1
            ans+=nice
        
        return ans
            