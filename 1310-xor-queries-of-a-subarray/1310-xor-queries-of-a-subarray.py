class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        prefix = [arr[0]]
        
        for i in range(1, len(arr)):
            val = prefix[i-1] ^ arr[i]
            prefix.append(val)
        
        for q in queries:
            s=q[0]
            e=q[1]
            
            if s==0:
                ans.append(prefix[e])
            else:
                ans.append(prefix[e] ^ prefix[s-1])
        
        return ans
        
        
        
        
        
#         BRUTE
#         for q in queries:
#             xor=0
#             for j in range(q[0], q[1]+1):
#                 xor ^= arr[j]
            
#             ans.append(xor)
        
#         return ans