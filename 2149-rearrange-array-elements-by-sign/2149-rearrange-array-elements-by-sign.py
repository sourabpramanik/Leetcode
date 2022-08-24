class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:                
        ans = [0] * len(nums)
        pos, neg = 0, 1
        
        
        for v in nums:
            if v>=0:
                ans[pos] = v
                pos+=2
            else:
                ans[neg] = v
                neg+=2
      
        
        return ans
       
            