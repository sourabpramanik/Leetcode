class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        obj = {}
        
        for v in nums:
            if v%2==0:
                if not v in obj:
                    obj[v] = 1
                else:
                    obj[v]+=1
        
        if len(obj) ==0: return -1
            
        key=float("inf")        
        val=float("-inf")
        
        for v in obj:
            if(obj[v]>val):                
                key = v 
                val = obj[v]
            elif(obj[v]==val):
                key = min(key, v)
        
        return key