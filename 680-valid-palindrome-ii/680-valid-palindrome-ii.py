class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0,len(s)-1
        
        while low<high:
            if s[low]==s[high]:
                low+=1
                high-=1
            else:
                return self.util(s, low, high-1) or self.util(s, low+1, high)
        return True
    
    def util(self, s, low, high):
        while low< high:
            if s[low]==s[high]:
                low+=1
                high-=1
            else:
                return False
        return True
                
    