class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:                
        count=0
        numStr=str(num)
        
        for i in range(0, len(numStr)-k+1): 
            sub = int(numStr[i:k+i])
            
            if sub!=0:
                if num % sub==0:
                    count+=1   
        
        return count