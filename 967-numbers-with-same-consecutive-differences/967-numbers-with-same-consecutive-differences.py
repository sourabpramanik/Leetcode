class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res=[]
        
        def rec(num, n, K, res):
            if n==0:
                res.append(num)
            else:
                dig=num % 10
            
                if dig+K <= 9:                
                    rec(num * 10 + dig + K, n - 1, K, res)

                if (K != 0 and dig >= K):
                    rec(num * 10 + dig - K, n - 1, K, res)
        
        for i in range(1, 10):
            rec(i, n-1, k, res)
        
        return res
                