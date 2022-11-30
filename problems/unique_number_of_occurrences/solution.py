class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur={}
        j=0
        for num in arr:
            occur[num]=occur.get(num, 0)+1
        
        if len(set(occur.values()))!=len(set(arr)):
            return False
            
        return True    
            