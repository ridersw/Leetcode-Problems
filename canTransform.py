class Solution:
    def canTransform(self, start, end):
        if len(start) < 2:
            return start == end

        print(f'start == end: {start == end}')
        if start == end:
            return True

        print(f'Can Transform Called')
        for swi in range(len(start)-1):
            print(f'Checking the chars at {swi}:{start[swi]} and {swi+1}:{start[swi+1]}')
            if start[swi] == end[swi+1] and start[swi+1] == end[swi] and start[swi] != start[swi+1]:
                if start[swi] != 'R' and start[swi+1] != 'L' and start[swi] != 'L' and start[swi+1] != 'R': 
                    print(f'Exchange match found at {swi} and {swi+1}')
                    print(f'start before interchange: {start}')
                    start = list(start)
                    start[swi], start[swi+1] = start[swi+1], start[swi]
                    start = "".join(start)
                    print(f'start after interchange: {start}')
                    return self.canTransform(start, end) 

        return start == end

if __name__ == "__main__":
    obj = Solution()
    # print(obj.canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))
    # print(obj.canTransform(start = "X", end = "L"))
    print(obj.canTransform(start = "RL", end = "LR"))