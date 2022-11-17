class MemoryManagement:
    def __init__(self):
        self.indexes = {}
        self.preAllocated = []


    def management(self, memory, queries):
        res=  []
        for swi in range(len(memory)):
            if memory[swi] == 1:
                self.preAllocated.append(swi)
        for query in queries:
            if query[0] == 'alloc':
                ans = self.alloc(query[1])
            else:
                ans = self.free(query[1])
            res.append(ans)
        return res

    def alloc(self, memoryUnits):
        memoryUnits = int(memoryUnits)
        for swi in range(0, len(memory), 8):
            if memory[swi] == 0 and 1 not in memory[swi:swi+memoryUnits]:
                for swj in range(swi, swi+memoryUnits):
                    memory[swj] = 1

                self.indexes[swi] = memoryUnits
                return swi  
        return -1

    def free(self, index):
        index = int(index)
        if index in self.indexes:
            length = self.indexes[index]
            self.indexes.pop(index)

            for swi in range(index, index+length):
                memory[swi] = 0

            return length

        elif index in self.preAllocated:
            memory[index] = 0
            self.preAllocated.remove(index)
            return 1
        else:
            return -1


if __name__ == "__main__":
    obj = MemoryManagement()

    memory = [0,1,0,0,0,1,1,0,0,0,0,0,1,1,1,1]

    queries = [['alloc', '2'],['alloc', '1'],['alloc','1'],['free','0'],['free','9'],['free','8'],['alloc','3'],['free','5'], ['alloc', '4']]

    #memory = []


    print(f'Ans: {obj.management(memory, queries)}')
    print(f'Updated Memory: {memory}')
    print(f'indexes: {obj.indexes}')