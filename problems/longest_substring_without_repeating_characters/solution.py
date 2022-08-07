class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longer = 0
        subStr = ""
        for ch in s:
            if ch not in subStr:
                subStr += ch                       
            else:
                subStr = subStr[subStr.find(ch) + 1:] + ch
            
            if(len(subStr) > longer):
                longer = len(subStr)
                
        return longer