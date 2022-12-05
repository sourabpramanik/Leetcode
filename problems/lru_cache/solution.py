class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node(-1, -1)
        self.tail=Node(-1, -1)
        self.cap=capacity
        self.map={}
        
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key in self.map:
            adrs = self.map[key]
            res=adrs.val
            self.map.pop(key)
            self.deleteNode(adrs)
            self.addNode(Node(key, res))
            self.map[key]=self.head.next
            return res
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            adrs = self.map[key]
            res=adrs.val
            self.map.pop(key)
            self.deleteNode(adrs)
        
        if len(self.map)==self.cap:
            self.map.pop(self.tail.prev.key)
            self.deleteNode(self.tail.prev)
            
        self.addNode(Node(key, value))
        self.map[key]=self.head.next
    
    def addNode(self, node):
        temp=self.head.next
        node.next=temp
        node.prev=self.head
        self.head.next=node
        temp.prev=node
    
    def deleteNode(self, node):
        dlPrev=node.prev
        dlNext=node.next
        dlPrev.next=dlNext
        dlNext.prev=dlPrev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)