class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1, -1]    
        
        if(len(nums)<1): return ans
        
        s=0
        e=len(nums)-1
        while(s<=e):
            mid=s+(e-s)//2
            
            if(nums[mid]<=target):
                s=mid+1
            else:
                e=mid-1
            if(nums[mid]==target):
                ans[1]=mid
        
        s=0
        e=len(nums)-1
        
        while(s<=e):
            mid=s+(e-s)//2
            
            if(nums[mid]>=target):
                e=mid-1  
            else:
                s=mid+1
            
            if(nums[mid]==target):
                ans[0]=mid
                
                
        
        return ans
                