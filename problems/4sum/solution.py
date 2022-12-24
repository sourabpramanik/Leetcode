class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(0, n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            first=nums[i]
            for j in range(i+1, n-1):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                second=nums[j]
                diff=target-first-second
                l=j+1
                r=n-1
                while l<r:
                    rem=nums[l]+nums[r]
                    if rem==diff:
                        ans.append([first, second, nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif rem>diff:
                        r-=1
                    else:
                        l+=1
        return ans
                        