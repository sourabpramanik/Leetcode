class Solution:
    def frequencySort(self, s: str) -> str:
        m = dict()
        res=""
        for v in s:
            m[v] = m.get(v, 0) + 1
        
        for k, v in sorted(m.items(), key=lambda x: x[1], reverse=True):
            res+=k * v
        
        return res