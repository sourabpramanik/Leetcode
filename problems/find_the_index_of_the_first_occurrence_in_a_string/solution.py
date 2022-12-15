class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)

        s=0
        for e in range(0, len(haystack)):
            if e-s==k-1:
                if haystack[s:e+1]==needle:
                    return s
                s+=1
        return -1