class MinStack:

    def __init__(self):
        self.st=[]
        self.min=float("inf")

    def push(self, val: int) -> None:
        if not self.st:
           self.st.append(val)
           self.min=val
        else:
            if val<self.min:
                self.st.append(2*val-self.min)
                self.min=val
            else:
                self.st.append(val)      

    def pop(self) -> None:
        if self.st:
            val=self.st.pop()
            if val<self.min:                
                self.min=2*self.min-val            

    def top(self) -> int:
        val=-1
        if self.st:
            val=self.st[-1]
            if val<self.min:                
                val=self.min 
        return val

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()