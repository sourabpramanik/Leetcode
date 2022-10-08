class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s=0
        curr=0
        count=float(inf)
        
        for e in range(0, len(blocks)):
            if blocks[e]=="W":
                curr+=1
            
            if e>=k-1:
                count = min(count, curr)
                
                if blocks[s]=="W":
                    curr-=1
                s+=1
                    
        
        return count if count>=0 else 0
                