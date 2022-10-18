class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        m = dict()
        
        for v in nums:
            m[v] = m.get(v, 0) + 1
        
        res = []
        
        for k, v in sorted(m.items(), key=lambda x:x[1], reverse=True):
            res.append(k)
            t-=1
            if t==0:
                return res
        