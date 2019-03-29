from collections import deque

class LRUCache:
    d = {}
    capacity = 0
    q = deque()
    def __init__(self, capacity: int):
        self.capacity = capacity        

    def get(self, key: int) -> int:
        if key in self.d:
            self.q.append(self.q.popleft())
            return self.d[key]
        else:
            return -1       

    def put(self, key: int, value: int) -> None:
        if len(self.d) == self.capacity:
            print("************",self.d.pop(self.q.popleft(), None))
        self.d[key] = value
        self.q.append(key)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)
obj.put(2,1)
print(obj.get(2))
obj.put(3,2)
print(obj.get(2))
print(obj.get(3))