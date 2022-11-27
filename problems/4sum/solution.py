class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        for i in range(0, n):
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1, n):
                if j>i+1 and nums[j-1]==nums[j]:
                    continue
                l=j+1
                r=len(nums)-1
                diff=target-nums[i]-nums[j]
                while l<r:
                    val=nums[l]+nums[r]
                    if diff==val:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif diff<val:
                        r-=1
                    else:
                        l+=1
                        
        
        return ans