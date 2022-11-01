class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = [0]*len(words)
        ans = 0
        
        for i, word in enumerate(words):
            for ch in word:
                mask[i] = mask[i] | 1<<(ord(ch) - ord("a"))
            
            for j in range(i):
                if not mask[i] & mask[j]:
                    ans = max(ans, len(words[i])*len(words[j]))
        
        return ans
        
        
        
        
        
        
        
#           BRUTE
#         maxL = 0
#         n = len(words)
#         for i in range(0, n):
#             j=i+1
#             m = Counter(words[i])
            
#             while j<n:
#                 if not self.common(words[i], words[j]):
#                     maxL = max(maxL, len(words[i])*len(words[j]))
#                 j+=1
                
#         return maxL
    
#     def common(self, w1, w2):
#         m = Counter(w1)
#         for l in w2:
#             if l in m:
#                 return True
        
#         return False