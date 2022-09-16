class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c, a = Counter(changed), []
        
        
        for num in sorted(changed, key = lambda x: abs(x)):
            if c[num]==0: continue
            if c[num*2]==0: return []
            
            a += [num]
            if num==0 and c[num]<=1: return []
            c[num]-=1
            c[num*2]-=1
        
        return a
                        
        
            
                
        
        