class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dic = {}
        ans = 1
        for num in nums:
            dic[num]=1
        
        for i in range(0, len(nums)):
            val=nums[i]
            if not val-1 in dic:
                curr = 1
                p = val+1
                while p in dic:
                    curr+=1
                    p+=1
                ans = max(ans, curr)
        return ans