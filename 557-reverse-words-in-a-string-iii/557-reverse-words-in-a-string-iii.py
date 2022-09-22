class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        for v in s.split(" "):
            v = v[::-1]
            words.append(v)
            
        print(words)  
        return (" ").join(words)
        
        
        