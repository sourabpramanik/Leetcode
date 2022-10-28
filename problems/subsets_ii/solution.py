class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        nums.sort()
        for i in range(0, (1<<len(nums))):
            self.bitMap(nums, seen, ans, i)
        
        return ans
    
    def bitMap(self, nums, seen, ans, i):
        j=0
        v=[]
        
        while i>0:
            
            if i&1:
                v.append(nums[j])
            j+=1
            i = i>>1
        tup = tuple(v)
        if tup not in seen:
            seen.add(tup)
            ans.append(v)
        return
        