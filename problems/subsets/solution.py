class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0, (1<<len(nums))):
            self.bitManp(nums, ans, i)
        
        return ans
    def bitManp(self, nums, ans, i):
        j=0
        v = []
        while i>0:
            if(i&1==1):
                v.append(nums[j])
            j+=1
            i=i>>1
        
        ans.append(v)
        return