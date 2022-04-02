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

# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

# Example 1:


# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# Example 2:

# Input: start = "X", end = "L"
# Output: false
 

# Constraints:

# 1 <= start.length <= 104
# start.length == end.length
# Both start and end will only consist of characters in 'L', 'R', and 'X'.