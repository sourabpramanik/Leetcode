class Solution:
    def frequencySort(self, s: str) -> str:
        
        counter={}
        
        for c in s:
            counter[c] = counter.get(c, 0)+1
                
        ans=""
        for k in dict(sorted(counter.items(), key=lambda x:x[1], reverse=True)):
            while counter[k]!=0:
                ans+=k
                counter[k]-=1
            
        return ans