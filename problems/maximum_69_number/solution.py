class Solution:
    def maximum69Number (self, num: int) -> int:
        curr = 0
        maxi = num
        num = str(num)
        
        for i in range(0, len(num)):
            
            if num[i]=="6":
                curr = num[:i]+"9"+num[i+1:]
            elif num[i]=="9":
                curr = num[:i]+"6"+num[i+1:]
            
            maxi = max(maxi, int(curr))
        
        return maxi
            
                