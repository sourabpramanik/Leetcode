class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = []
        i=1
        
        while len(ans)<k:
            
            if not i in arr:
                ans.append(i)
            i+=1
        return ans[-1]