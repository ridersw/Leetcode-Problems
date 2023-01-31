class Solution:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = []
        self.keys = []

    def get(self, key: int) -> int:
        if key in self.keys:
            for d in self.data:
                if d[0] == key:
                    temp = d
                    self.data.remove(temp)
                    self.data.append(temp)
                    break
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            for d in self.data:
                if d[0] == key:
                    temp = d
                    self.data.remove(temp)
                    self.data.append(temp)
                    break
        else:
            if self.capacity == len(self.data):
                self.data = self.data[1:]
            self.data.append([key, value])


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