class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n=len(nums)
        store={}
        for i, num in enumerate(nums):
            store[num] = i
            
        ans=0
        for i in range(0,n):
            if not nums[i]-1 in store:
                p=nums[i]
                count=0
                while p in store:
                    count+=1
                    p+=1
                
                ans=max(ans, count)
        
        return ans