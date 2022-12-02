class MyStack:

    def __init__(self):
        self.queue=Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        if self.queue.size==0:
            return -1
        return self.queue.pop()

    def top(self) -> int:
        if self.queue.size==0:
            return -1
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.isEmpty()
class Queue:
    def __init__(self):
        self.arr=[]
    
    def push(self, data):
        self.arr.append(data)
    
    def peek(self):
        return self.arr[-1]
            
    def pop(self):
        return self.arr.pop(self.size()-1)
    
    def size(self):
        return len(self.arr)
    
    def isEmpty(self):
        if self.size()==0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()