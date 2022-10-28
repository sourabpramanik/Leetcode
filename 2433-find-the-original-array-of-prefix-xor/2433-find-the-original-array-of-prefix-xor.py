class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        ans.append(pref[0])
        
        for i in range(1, len(pref)):
            n = pref[i-1]^pref[i]
            ans.append(n)

        return ans