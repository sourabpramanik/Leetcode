class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = {}
        
        for v in nums:
            m[v] = m.get(v, 0) + 1 
        
        dup=-1
        miss=1
        
        for i in range(1, len(nums)+1):
            if i in m:
                if m[i]==2:
                    dup=i
            else:
                miss=i
        
        return [dup, miss]
        