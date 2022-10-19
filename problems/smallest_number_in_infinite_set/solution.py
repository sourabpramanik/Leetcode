import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.num = 1
        self.h = []

    def popSmallest(self) -> int:
        if len(self.h):
            return heapq.heappop(self.h)
            
        curr = self.num
        self.num+=1        
        return curr

    def addBack(self, N: int) -> None:
        if N < self.num and N not in self.h:
            heapq.heappush(self.h, N)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)