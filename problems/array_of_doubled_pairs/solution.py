class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)       
        
        for v in sorted(arr, key = lambda x: abs(x) ):
            if c[v]==0: continue
            if c[v*2]==0: return False
            
            c[v]-=1            
            c[v*2]-=1
        
        return True