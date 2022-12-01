class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1, -1]    
        
        if(len(nums)<1): return ans
        
        s=0
        e=len(nums)-1
        while(s<=e):
            mid=s+(e-s)//2
            if(nums[mid]==target):
                ans[1]=mid
            if(nums[mid]<=target):
                s=mid+1
            else:
                e=mid-1
            
        
        s=0
        e=len(nums)-1
        
        while(s<=e):
            mid=s+(e-s)//2
            
            if(nums[mid]==target):
                ans[0]=mid
            if(nums[mid]<target):
                s=mid+1
            else:
                e=mid-1
            
            
                
                
        
        return ans