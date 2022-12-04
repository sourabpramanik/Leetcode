class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n=len(nums)
        arr=[]
        for i in range(0, n):
            arr.append(nums[i])
        arr.sort()
        
        l=0
        r=n-1
        
        n1=0
        n2=0
        
        while l<r:
            if arr[l]+arr[r]==target:
                n1=arr[l]
                n2=arr[r]
                break
            elif arr[l]+arr[r]>target:
                r-=1
            else:
                l+=1
                
        ans=[]
        for i in range(0, n):
            if nums[i]==n1:                
                ans.append(i)
            elif nums[i]==n2:                
                ans.append(i)
        return ans
        
        
        