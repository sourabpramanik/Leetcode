class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        pq = collections.deque()
        m = dict()
        
        for v in arr:
            m[v] = m.get(v, 0) + 1
        
        for k in m:
            pq.append(m[k])
            
        count = 0
        res = 0
        pq = sorted(pq)
        while pq:
            res+=1
            count += pq.pop()
            if count >= len(arr)/2:
                return res
        
        return 0