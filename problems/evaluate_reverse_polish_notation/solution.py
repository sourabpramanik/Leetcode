class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
  
        for i in range(0, len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                r=stack.pop()
                l=stack.pop()
                val=0
                if tokens[i]=="+":
                    stack.append(l+r)
                elif tokens[i]=="-":
                    stack.append(l-r)
                elif tokens[i]=="*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l/r)))
            
        return stack.pop()