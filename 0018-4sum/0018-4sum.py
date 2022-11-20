class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums.sort()
        for i in range(0,n):                                   
            for j in range(i+1,n):                
                diff = target-(nums[i]+nums[j])                  
                l=j+1
                r=n-1
                while l<r:
                    val = nums[l]+nums[r]
                    if val==diff:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                                                      
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1 
                        l+=1
                        r-=1

                    elif val>diff:
                        r-=1
                    else:
                        l+=1
            
        
        return ans