class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cap=capacity
        self.size=0
        self.store=dict()
    def get(self, key: int) -> int:
        res=-1
        if key in self.store:
            node = self.store[key]
            res = node.val
            self.delNode(node)
            self.addNode(Node(key,res))
            self.store[key]=self.head.next
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            self.store.pop(key)
            self.delNode(node)
            self.size-=1

        if self.cap==self.size:
            self.store.pop(self.tail.prev.key)
            self.delNode(self.tail.prev)
            self.size-=1

        node = Node(key, value)
        self.addNode(node)
        self.store[key] = self.head.next
        self.size+=1

    def addNode(self, node):
        temp = self.head.next
        self.head.next=node
        temp.prev=node
        node.next=temp
        node.prev=self.head

    def delNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)