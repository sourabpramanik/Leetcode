class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        n=len(nums)
        temp=[]
        for num in nums:
            temp.append(num)
        temp.sort()

        l=0
        r=n-1
        n1=0
        n2=0

        while l<r:
            if temp[l]+temp[r]==target:
                n1=temp[l]
                n2=temp[r]
                break
            elif temp[l]+temp[r]>target:
                r-=1
            else:
                l+=1
        
        for i, num in enumerate(nums):
            if num==n1:
                ans.append(i)
            elif num==n2:
                ans.append(i)
        
        return ans
    
                