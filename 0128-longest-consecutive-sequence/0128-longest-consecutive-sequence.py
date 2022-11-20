class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans = 1
        count=1
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]!=nums[i]:
                if nums[i-1]+1==nums[i]:
                    count+=1
                else:
                    ans=max(ans, count)
                    count=1
        
        return max(ans, count)