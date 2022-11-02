class Solution:
    def program(self, memory, queries):
        res = []

        length = len(memory)
        memory_staring_index = []
        memory_block = {}
        default_memory_block = []

        count = 0

        for swi in range(len(memory)):
            if memory[swi] == 1:
                default_memory_block.append(swi)
                

        while count < length:
            memory_staring_index.append(count + 8)
            count += 8

        for query in queries:
            print(f'Operation: {query[0]} and Para: {query[1]}')
            flag = False
            if query[0] == 'alloc':
                for msi in memory_staring_index:
                    if memory[msi] == 0 and 1 not in memory[msi:msi+int(query[1])]:
                        print(f'Checking 0 for memory[msi,msi+int(query[1])]: {memory[msi:msi+int(query[1])]} and int(query[1]): {msi+int(query[1])} and msi+int(query[1]): {msi+int(query[1])}')
                        for swi in range(msi,msi+int(query[1])):
                            memory[swi] = 1
                            flag = True
                            memory_block[msi] = int(query[1])
                        print('Line 30')
                        res.append(msi)
            else:
                if int(query[1]) in memory_block:
                    for swi in range(int(query[1]), memory_block[query[1]]):
                        memory[swi] = 0
                    res.append(int(query[1]))
                    print('Line 37')
                    memory_block.pop(query[1])
                    

                elif int(query[1]) in default_memory_block:
                    memory[int(query[1])] = 0
                    default_memory_block.remove(int(query[1]))
                    res.append(1)
                    print('Line 44')
                    
                else:
                    res.append(-1)
                    print('Line 49')
                flag = True
    
            if not flag:
                res.append(-1)
                print('Line 54')

        return res


if __name__ == "__main__":
    obj = Solution()

    memory = [0,1,0,0,0,1,1,0,0,0,0,0,1,1,1,1]
    queries = [["alloc", '2'],['alloc','1'],['alloc','1'],['free','0'],['free','9'],['free','8'],['alloc','3'],['free','5'],['alloc', '4']]

    print(obj.program(memory, queries))