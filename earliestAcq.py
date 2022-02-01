class Solution:
    def earliestAcq(self, logs, n):

        logs.sort(key = lambda x:x[0])

        print(f'logs: {logs}')
        
        friendList = []

        for swi in range(len(logs)):
            # print(f'checking for {[logs[swi][1]]}')
            if [logs[swi][1]] not in friendList:
                friendList.append([logs[swi][1]])
            # print(f'checking for {[logs[swi][2]]}')
            if [logs[swi][2]] not in friendList:
                friendList.append([logs[swi][2]])

        friendList.sort()

        print(f'friendList: {friendList}')

        for log in logs:
            
            friend1 = log[1]
            friend2 = log[2]
            friend1Index = None
            friend2Index = None

            for swi in range(len(friendList)):
                if friend1 in friendList[swi] and not friend1Index:
                    friend1Index = swi

                if friend2 in friendList[swi] and not friend2Index:
                    friend2Index = swi

            if friend1Index != friend2Index:
                friendList[friend1Index].extend(friendList[friend2Index])
                friendList.remove(friendList[friend2Index])

            if len(friendList) == 1:
                print(f'Returning to main friendList: {friendList}')
                return log[0]

            print(f'friendList: {friendList}')

        return -1        


if __name__ == "__main__":
    obj = Solution()

    # print(obj.earliestAcq(logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6))


    # print(obj.earliestAcq(logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4))

    #print(obj.earliestAcq(logs = [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]], n = 4))

    # print(obj.earliestAcq(logs = [[0,2,0],[7,4,3],[2,2,1],[1,0,1],[5,4,1],[6,3,2],[8,3,1],[3,0,4]], n = 5))

    print(obj.earliestAcq(logs = [[9,0,3],[0,2,7],[12,3,1],[5,5,2],[3,4,5],[1,5,0],[6,2,4],[2,5,3],[7,7,3]], n = 8))

# There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

# Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

# Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.

 

# Example 1:

# Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
# Output: 20190301
# Explanation: 
# The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
# The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
# The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
# The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
# The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friends anything happens.
# The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.
# Example 2:

# Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
# Output: 3
 

# Constraints:

# 2 <= n <= 100
# 1 <= logs.length <= 104
# logs[i].length == 3
# 0 <= timestampi <= 109
# 0 <= xi, yi <= n - 1
# xi != yi
# All the values timestampi are unique.
# All the pairs (xi, yi) occur at most one time in the input.