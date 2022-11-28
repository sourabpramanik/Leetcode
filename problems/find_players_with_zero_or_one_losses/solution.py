class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[[],[]]
        
        hashMap={}
        for a in matches:
            hashMap[a[0]]=0            
        for a in matches:
            hashMap[a[1]]=hashMap.get(a[1], 0)+1
        for p in hashMap:
            if hashMap[p]==0:
                ans[0].append(p)
            if hashMap[p]==1:
                ans[1].append(p)
        ans[0].sort()        
        ans[1].sort()
        return ans