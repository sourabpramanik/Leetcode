class RandomizedSet:

    def __init__(self):
        self.ds={}
        self.arr=[]       

    def insert(self, val: int) -> bool:
        if val in self.ds:
            return False
        
        self.ds[val]=len(self.arr)     
        self.arr.append(val)            
        return True
            

    def remove(self, val: int) -> bool:
        n=len(self.arr)   
        
        if val in self.ds:            
            
            lastElement = self.arr[-1]
            idx = self.ds[val]
            
            self.ds[lastElement]=idx
            
            self.arr[idx] = lastElement
            self.arr[-1] = val
            self.arr.pop(n-1)
            
            self.ds.pop(val)
            
            return True   
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()