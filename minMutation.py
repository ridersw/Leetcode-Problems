
class Solution:
    # def checkMutation(self, start, end, bank, count):
    #     print(f'start: {start} end: {end} count: {count}')
    #     if start == end:
    #         return count

    #     start = list(start)
    #     for swi in range(len(start)):
    #         print(f'checking for Character: start: {start[swi]} and end: {end[swi]}')
    #         if start[swi] != end[swi]:
    #             print(f'Mismatch found for Character: start: {start[swi]} and end: {end[swi]}')
    #             tempStart = start[:swi] + [end[swi]] + start[swi+1:]
    #             tempStart = "".join(tempStart)
    #             print(f'tempStart: {tempStart}')
    #             if tempStart in bank:
    #                 print(f'temp: {tempStart}')
    #                 start = tempStart
    #                 count += 1
    #                 self.checkMutation(start, end, bank, count)
    #     print(f'final count: {count}')
    #     if count == 0:
    #         return -1
    #     else:
    #         return count

    def minMutation(self, start, end, bank, count = 0):
        
        #return self.checkMutation(start, end, bank, count=0)
        print(f'line 30) start: {start} end: {end} count: {count}')
        if start == end:
            print(f'start == end')
            return count

        start = list(start)
        for swi in range(len(start)):
            print(f'checking for Character: start: {start[swi]} and end: {end[swi]}')
            if start[swi] != end[swi]:
                print(f'Mismatch found for Character: start: {start[swi]} and end: {end[swi]}')
                tempStart = start[:swi] + [end[swi]] + start[swi+1:]
                tempStart = "".join(tempStart)
                print(f'tempStart: {tempStart}')
                if tempStart in bank:
                    print(f'temp: {tempStart}')
                    start = tempStart
                    count += 1
                    count = self.minMutation(start, end, bank, count)
        print(f'final count: {count}')
        if count == 0:
            return -1
        else:
            return count

    

            

if __name__ == "__main__":
    obj = Solution()

    #print(obj.minMutation(start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]))
    #print(obj.minMutation(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
    print(obj.minMutation(start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]))

