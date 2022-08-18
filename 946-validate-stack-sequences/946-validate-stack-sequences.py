class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        i = 0
        j = 0
        
        for num in pushed:
            pushed[i] = num
            
            while i >= 0 and pushed[i] == popped[j]:
                i-=1
                j+=1
            i+=1
           
        return i == 0