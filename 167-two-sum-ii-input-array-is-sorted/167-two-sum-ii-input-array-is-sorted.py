class Solution:
    def twoSum(self, N: List[int], target: int) -> List[int]:
        l=0
        r=len(N)-1
        
        while l<=r:
            
            
            if N[l]+N[r]==target:
                return [l+1, r+1]
            elif N[l]+N[r]>target:
                r-=1
            else:
                l+=1
        
        return []