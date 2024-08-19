class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #cache stores the key and the values. Each key-value pairs 
                        ##linked to the corresponding node 
        #LRU: left-most node, most recent: right nodes
        self.left, self.right = ListNode(0,0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prev
        prev.next = nxt.prev = node
        

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

        

    def get(self, key: int) -> int:
        if key in self.cache:
        #update the value if the key exists
            self.remove(self.cache[key]) #remove the pointer poiting to the node 
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #remove the existing node before adding the 
                                            ##updated one
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)