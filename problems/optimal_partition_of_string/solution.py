class Solution:
    def partitionString(self, s: str) -> int:
        aux = ""
        count= 1
        
        for v in s:
            if not v in aux:
                aux+=v
            else:
                count+=1
                aux=v
        return count