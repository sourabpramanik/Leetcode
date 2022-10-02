
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        minVal = min(a, b)
        arr=[]
        
        for i in range(1, minVal+1):
            arr.append(i)
        
        j=0
        count=0
        while j<len(arr):
            
            if a%arr[j]==0 and b%arr[j]==0:
                count+=1
            
            j+=1
        
        return count
        
            
            
        