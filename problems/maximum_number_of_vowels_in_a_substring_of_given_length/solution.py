class Solution:
    def maxVowels(self, word: str, k: int) -> int:
        vow = ["a", "e", "i", "o", "u"]
        s=0
        count=float(-inf)
        curr=0
        
        for e in range(0, len(word)):
            if word[e] in vow:
                curr+=1
            
            if e>=k-1:
                count = max(count, curr)
                if word[s] in vow:
                    curr-=1
                s+=1
        return count