class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels="aeiouAEIOU"
        n=len(s)
        i=0
        j=n//2
        c1=0
        c2=0
        while i<n//2 and j<n:
            if s[i] in vowels:
                c1+=1
            if s[j] in vowels:
                c2+=1
            
            i+=1
            j+=1
        
        return c1==c2