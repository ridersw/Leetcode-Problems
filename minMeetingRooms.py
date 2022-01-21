
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        starts = []
        ends = []
        
        for start, end in intervals:
            starts.append(start)
            ends.append(end)
            
        starts.sort()
        ends.sort()
        
        room = 0
        endp = 0
        
        for swi in range(len(starts)):
            if starts[swi] >= ends[endp]:
                endp += 1
            else:
                room += 1
                
        return room

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106