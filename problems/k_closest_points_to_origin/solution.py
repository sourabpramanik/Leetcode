import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        h=[]
        
        for p in points:
            
            if len(h)<=K-1:
                heapq.heappush(h, (-p[0]**2-p[1]**2, p))
            elif (-p[0]**2-p[1]**2) > h[0][0]:
                heapq.heapreplace(h,(-p[0]**2-p[1]**2,p))
        
        res = []
        while K:
            res.append(heapq.heappop(h)[1])
            K-=1
        
        return res