class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs)==0:
            return ""

        short=min(strs, key=len)

        for i, c in enumerate(short):
            for s in strs:
                if s[i]!=c:
                    return short[:i]
        return short