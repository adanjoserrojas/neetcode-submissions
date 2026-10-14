class MyHashMap:

    def __init__(self):
        self.hashmap: dict = {}

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key] = value
        self.hashmap.setdefault(key, value)
        return

    def get(self, key: int) -> int:
        return self.hashmap.get(key, -1)
        

    def remove(self, key: int) -> None:
        if key in self.hashmap:
            del self.hashmap[key]
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)