class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key= lambda x: (x[0], -x[1]))
        
        count = 0
        minm = float("-inf")
        
        for v in range(len(properties)-1, -1, -1):
            if(properties[v][1]<minm):
                count+=1
            
            minm = max(properties[v][1], minm)
        
        return count