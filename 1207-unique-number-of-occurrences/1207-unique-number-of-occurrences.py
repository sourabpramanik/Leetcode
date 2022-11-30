class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur=set()
        arr.sort()
        i=0
        j=0
        while j<len(arr):
            if arr[i]!=arr[j]:
                dif = j-i
                if dif in occur:
                    return False
                occur.add(j-i)
                i=j
            
            j+=1
        dif = j-i
        if dif in occur:
            return False
        return True    
            