import math
class Solution:
    def kClosest(self, points: List[List[int]], t: int) -> List[List[int]]:
        m=defaultdict(list)
        for v in points:
            k = self.getSqrt(v[0], v[1])
            m[k].append(v)
        
        print(m)
        res = []
        for k, v in sorted(m.items(), key=lambda x: x[0]):
            for e in v:
                res.append(e)
                t-=1
                if t==0:
                    return res
        
        
        
    def getSqrt(self, x, y):
        return math.sqrt((0-x)**2 + (0-y)**2)