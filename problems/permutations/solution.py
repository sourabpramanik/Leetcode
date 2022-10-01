class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        freq = {}
        for i in range(len(nums)):
            freq[i] = 0
        
        def rec(ds):
            if len(ds)==len(nums):
                ans.append(ds[:])
                return
            
            for j in range(0, len(nums)):
                if freq[j]==0:
                    
                    freq[j] = 1
                    ds.append(nums[j])   
                    
                    rec(ds)
                    
                    ds.pop(len(ds)-1)
                    freq[j]=0                
        rec([])
        return ans