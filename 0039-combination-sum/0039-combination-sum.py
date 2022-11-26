class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        ans=[]
        
        def find(i, ds, targetSum):
            if i>=len(arr):
                return
            
            if targetSum==0:
                ans.append(ds[:])
                return
            
            if targetSum>=arr[i]:
                ds.append(arr[i])
                find(i, ds, targetSum-arr[i])
                ds.pop(len(ds)-1)
            find(i+1, ds, targetSum)
        
        find(0, [], target)
        return ans