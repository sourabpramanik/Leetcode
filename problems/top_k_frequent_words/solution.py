class Solution:
    def topKFrequent(self, words: List[str], t: int) -> List[str]:
        m = dict()
        
        for v in words:
            m[v] = m.get(v, 0) + 1
        
        bucket = [0]*len(words)
        
        for k in m:
            v = m[k]
            if bucket[v]==0:
                bucket[v] = []
            bucket[v].append(k)
        
        res=[]
        for i in range(len(bucket)-1, -1, -1):
            v = bucket[i]
            if v!=0:
                v.sort()
                for e in v:
                    res.append(e)
                    t-=1
                    if t==0:
                        return res