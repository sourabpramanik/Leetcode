class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        m = dict()
        
        for v in nums:
            m[v] = m.get(v, 0) + 1
        
        bucket = [0]* (len(nums)+1)
       
        
        for k in m:
            v = m[k]
            if bucket[v]==0:
                bucket[v] = []
            bucket[v].append(k)
        
        res = []
        
        for i in range(len(bucket)-1, -1, -1):
            arr = bucket[i]
            if arr!=0:
                for v in arr:
                    res.append(v)
                    t-=1
                    if t==0:
                        return res
        
        