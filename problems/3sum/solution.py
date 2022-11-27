class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(0, n):            
            if i!=0 and nums[i]==nums[i-1]:
                continue
            else:
                j=i+1
                k=n-1            
                while j<k:
                    val=nums[i]+nums[j]+nums[k]
                    if val==0:
                        ans.append([nums[i],nums[j],nums[k]])
                        while j<k and nums[j]==nums[j+1]:
                            j+=1
                        while j<k and nums[k]==nums[k-1]:
                            k-=1
                        j+=1
                        k-=1
                    elif val>0:
                        k-=1
                    else:
                        j+=1
        
        return ans
                