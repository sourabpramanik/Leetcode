class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(arr)
        arr.sort()
        def find(i, ds, targetSum):
            
            if targetSum==0:
                ans.append(ds[:])
                return
            
           
            
            
            for j in range(i, n):
                if targetSum<arr[j]: 
                    break
                if j>i and arr[j]==arr[j-1]:
                    continue
                ds.append(arr[j])
                find(j+1, ds, targetSum-arr[j])
                ds.pop(len(ds)-1)
            
        find(0, [], target)
        return ans