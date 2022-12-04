class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(0, n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n-1):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                r=n-1
                dif=target-nums[i]-nums[j]
                
                while l<r:
                    val=nums[l]+nums[r]
                    if val==dif:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        
                        l+=1
                        r-=1
                    elif val>dif:
                        r-=1
                    else:
                        l+=1
        
        return ans