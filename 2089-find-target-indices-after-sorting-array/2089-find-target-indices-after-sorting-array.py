class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        fo=-1
        lo=-1
        
        nums.sort()
        
        l=0
        h=len(nums)-1
        
        while l<=h:
            m = (l+h)//2
            
            if nums[m]==target:
                lo = m
                l = m+1
                continue
            
            if nums[m]<target:
                l=m+1
            else:
                h=m-1
        
        l=0
        h=len(nums)-1
        
        while l<=h:
            m = (l+h)//2
            
            if nums[m]==target:
                fo = m
                h = m-1
                continue
            
            if nums[m]<target:
                l=m+1
            else:
                h=m-1
                
        if fo==-1 and lo==-1:
            return []
        return [i for i  in range(fo, lo+1)]
    
        
        