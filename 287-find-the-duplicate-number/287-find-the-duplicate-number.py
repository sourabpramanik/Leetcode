class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        l, h= 1, len(nums)-1
        
        while(l<=h):
            c = 0
            m = (l+h)//2
            for v in nums:
                if(v<=m):
                    c+=1
            
            if c<=m:
                l=m+1
            else:
                h=m-1
        
        return l