class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        # O(n2)        
        # for i in range(0,n):            
        #     ans += [x+(1<<i) for x in reversed(ans)]
        
        # O(n)
        for i in range(1, 1<<n):
            ans.append(ans[-1] ^ (i & -i))
        return ans