class Solution:
    def maximum69Number (self, num: int) -> int:       
        s = str(num)
        
        for i in range(0, len(s)):
            if s[i]=="6":
                s = s[:i] + "9" + s[i+1:]
                return int(s)
        
        return num