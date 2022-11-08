class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i=0
        
        while i<len(s):
            if stack and abs(ord(s[i])-ord(stack[-1])) ==32:
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        
        return "".join(stack)
                