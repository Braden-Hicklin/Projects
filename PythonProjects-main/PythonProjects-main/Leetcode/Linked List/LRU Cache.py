class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()
        self.items = 0

    def get(self, key: int) -> int:
        try:
            self.cache.move_to_end(key)
            return self.cache[key]
        except:
            return -1

    def put(self, key: int, value: int) -> None:        
        if key not in self.cache:
            self.items += 1
        self.cache[key] = value
        self.cache.move_to_end(key)

        if self.items > self.cap:
            self.cache.popitem(last = False)
            self.items -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)