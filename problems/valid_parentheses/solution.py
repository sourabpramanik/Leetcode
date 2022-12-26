class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch=="(" or ch=="{" or ch=="[":
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                if (stack[-1]=="(" and ch==")") or (stack[-1]=="{" and ch=="}") or (stack[-1]=="[" and ch=="]"):
                    stack.pop()
                    continue
                else:
                    return False
        return len(stack)==0
