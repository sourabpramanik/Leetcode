class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        h=len(arr)-1
        
        while h-l>=k:
            if x-arr[l]<=arr[h]-x:
                h-=1
            else:
                l+=1
        
        return arr[l:h+1]