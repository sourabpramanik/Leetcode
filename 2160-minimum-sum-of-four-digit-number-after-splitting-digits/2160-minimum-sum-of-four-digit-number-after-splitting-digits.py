class Solution:
    def minimumSum(self, num: int) -> int:
        ds = []
        
        for _ in range(0, 4):
            ds.append(num%10)
            
            num//=10
        
        ds.sort()
        n1 = ds[0] *10 + ds[2]        
        n2 = ds[1] *10 + ds[3]
        
        return n1+n2