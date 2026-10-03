class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #key: node

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_right(self, node):
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # move to most recently used (rightmost)
            self.remove(self.cache[key]) #remove it
            self.insert_right(self.cache[key]) #insert to rightmost
            return self.cache[key].val #the value of the node
        return -1

    def put(self, key: int, value: int) -> None:
        #if key is already in cache, remove and insert again
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) #add to cache
        self.insert_right(self.cache[key]) #insert in LL

        if len(self.cache) > self.cap:
            #evict LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

