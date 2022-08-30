class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s=0
        e=len(nums)-1
        ans=0
        
        while(s<=e):
            mid=s+(e-s)//2
            
            if(nums[mid]>target):
                e=mid-1
            elif(nums[mid]<target):
                ans=mid+1                
                s=mid+1
            elif(nums[mid]==target):
                return mid
        return ans