class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def rec(i, arr):                 
            if(i==n):
                ans.append(arr[:])
                return
            
            for j in range(i, n):
                arr[i], arr[j] = arr[j], arr[i]
                rec(i+1, arr)      
                arr[i], arr[j] = arr[j], arr[i]
                
        
        rec(0, nums)
        return ans