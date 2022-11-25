class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            n=len(ans)
           
            for i in range(0, n):
                tmp=ans[i]+[num]
                ans+=[tmp]
                
            
            
        
        return ans
                
    