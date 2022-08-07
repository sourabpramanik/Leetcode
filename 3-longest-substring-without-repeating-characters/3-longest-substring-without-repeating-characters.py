class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longer = 0
        
        for i, ch in enumerate(s):
            a = ch
            j = i+1
            while(j<len(s) and (s[j] in a)==False):
                a += s[j]
                j+=1
            if(len(a) > longer):
                longer = len(a)
        return longer