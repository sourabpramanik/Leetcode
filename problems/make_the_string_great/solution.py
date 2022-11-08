class Solution:
    def makeGood(self, s: str) -> str:
        for i in range(len(s)-1):
            if abs(ord(s[i])-ord(s[i+1]))==32:
                return self.makeGood(s[:i]+s[i+2:])
        
        return s
        
#         stack = []
#         i=0
        
#         while i<len(s):
#             if stack and abs(ord(s[i])-ord(stack[-1])) ==32:
#                 stack.pop()
#             else:
#                 stack.append(s[i])
#             i+=1
        
#         return "".join(stack)
                