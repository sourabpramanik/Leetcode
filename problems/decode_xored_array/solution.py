class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = []
        ans.append(first)
        for v in encoded:
            n = v^ans[-1]
            ans.append(n)
        
        return ans