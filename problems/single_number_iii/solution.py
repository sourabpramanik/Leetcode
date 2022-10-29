class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for num in nums:
            xor ^= num
        
        id=0
        
        while xor:
            if xor&1:
                break
            id+=1
            xor = xor>>1
        
        xor1=0
        xor2=0
        
        for num in nums:
            if num & (1<<id):
                xor2^=num
            else:
                xor1^=num
        
        return [xor1, xor2]
    
    
    
#         LITTLE OPTIM
         # ans = []     
#         m = Counter(nums)
#         for k in m:
#             if m[k]==1:
#                 ans.append(k)
                
#         return ans
            
#         BRUTE
#         n = len(nums)
#         ans = []
#         for i in range(0, n):
#             c=0
#             for j in range(0, n):
#                 if nums[i]==nums[j]:
#                     c+=1
            
#             if c==1:
#                 ans.append(nums[i])
                
#         return ans

#         LESS BRUTE

          