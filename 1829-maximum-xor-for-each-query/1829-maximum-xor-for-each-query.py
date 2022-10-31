class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        XOR=0
        n=len(nums)
        ans = [0]*n
        for num in nums:
            XOR^=num
        
        XOR ^= (2**maximumBit) - 1
        # XOR ^= (1<<maximumBit) - 1
        ans[0] = XOR
        
        for i in range(1, n):
            XOR ^= nums[n-i]
            ans[i] = XOR
        
        return ans
        
#         BRUTE
#         m=2**(maximumBit)-1
#         ans = []
#         while len(nums)>0:
#             maxi=0
#             k=m
#             kth=0
#             while k>-1:
#                 xor = self.xorFunc(nums, k)
#                 if xor > maxi:
#                     maxi = xor
#                     kth= k
#                 k-=1
#             ans.append(kth)
#             nums.pop(len(nums)-1)
        
#         return ans
    
#     def xorFunc(self, nums, k):
#         xor = k
#         for v in nums:
#             xor ^= v
        
#         return xor