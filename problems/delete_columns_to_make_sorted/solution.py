class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        m=len(strs)
        n=len(strs[0])

        for j in range(0, n):
            for i in range(1, m):
                if strs[i][j]<strs[i-1][j]:
                    count+=1
                    break

        return count