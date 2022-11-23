class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        r=0
        ans=0
        n=len(nums)
        while r<n:
            if nums[r]==0:
                l=r+1
            r+=1
            ans=max(ans, r-l)
        
        return ans