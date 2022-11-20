class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans=1
        ds=Counter(nums)
        n=len(nums)
        for i in range(0,n):
            if not nums[i]+1 in ds:
                count=0
                p = nums[i]
                while p in ds:
                    count+=1
                    p-=1
                
                ans = max(ans, count)
        
        return ans
        