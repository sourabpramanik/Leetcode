class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        s=0
        e = len(A)-1
     
        while s<e:
            mid = (s+e)//2
            
            if A[mid]<A[mid+1]:
                s=mid+1
            else:
                e=mid
            
        return s