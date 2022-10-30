class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        s=-1
        res=1
        m=0
        
        for e in range(0, len(nums)):
            while nums[e]&m:
                s+=1
                m^=nums[s]
            m|=nums[e]
            res = max(res, e-s)
        
        return res