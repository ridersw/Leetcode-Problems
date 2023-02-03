from collections import defaultdict


class Solution:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        value = self.data.pop(key)
        self.data[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.pop(key)
        else:
            if len(self.data) == self.capacity:
                del self.data[next(iter(self.data))]
        self.data[key] = value

if __name__ == "__main__":
    lfu = Solution()
    lfu.put(1, 1);   
    lfu.put(2, 2);   
    lfu.get(1);      
                    
    lfu.put(3, 3);   
                    
    lfu.get(2);      
    lfu.get(3);     
                    
    lfu.put(4, 4);   
                   
    lfu.get(1);      
    lfu.get(3);      
                    
    lfu.get(4)