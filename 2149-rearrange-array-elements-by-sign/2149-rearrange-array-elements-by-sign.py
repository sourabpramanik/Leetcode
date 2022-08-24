class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:                
        pos, neg, ans = [], [], []
        flag, i = 1, 0
        
        
        for v in nums:
            if v>=0:
                pos.append(v)
            else:
                neg.append(v)
      
        pos = pos[::-1]
        neg = neg[::-1]
        while i<len(nums):
            if flag:
                val = pos.pop()
                ans.append(val)
                flag=0
            else:
                val = neg.pop()
                ans.append(val)
                flag=1
            i+=1
        
        return ans
       
            