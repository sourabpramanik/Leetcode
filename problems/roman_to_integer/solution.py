class Solution:
    def romanToInt(self, s: str) -> int: 
        trans={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,            
        }

        ans=0
        prev=""
        for i in range(len(s)-1, -1, -1):
            ch=s[i]
        
            if (prev=="V" or prev=="X") and ch=="I":                
                ans-=1
            elif (prev=="L" or prev=="C") and ch=="X":                
                ans-=10
            elif (prev=="D" or prev=="M") and ch=="C":                
                ans-=100
            else:
                ans+=trans[ch]
            
            prev=ch
        
        return ans