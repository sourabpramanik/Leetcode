class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels="aeiouAEIOU"
        count=0
        mid=len(s)//2
        
        for i, c in enumerate(s):
            if c in vowels:
                count+=1 if i < mid else -1
            
        return count==0