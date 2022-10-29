class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        m = Counter(nums)
        for k in m:
            if m[k]==1:
                ans.append(k)
                
        return ans
            
#         BRUTE
#         n = len(nums)
#         
#         for i in range(0, n):
#             c=0
#             for j in range(0, n):
#                 if nums[i]==nums[j]:
#                     c+=1
            
#             if c==1:
#                 ans.append(nums[i])
                
#         return ans

#         LESS BRUTE

          