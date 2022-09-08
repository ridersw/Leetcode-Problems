class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        pre_dict = {}
        edge_dict = {}
        
        for swi in range(numCourses):
            pre_dict[swi] = 0
            edge_dict[swi] = []
            
        for course, prerequisite in prerequisites:
            pre_dict[course] += 1
            edge_dict[prerequisite] += [course]
            
        my_que = deque()
        
        for i, v in pre_dict.items():
            if v== 0:
                my_que.append(i)
        
        # print(f'my_que: {my_que}')
        
        while my_que:
            pre_course = my_que.popleft()
            for course in edge_dict[pre_course]:
                pre_dict[course] -= 1
                if pre_dict[course] == 0 and course not in my_que:
                    my_que.append(course)
        return not any(pre_dict.values())
        
if __name__ == "__main__":
    obj = Solution()

    print(obj.canFinish(numCourses = 2, prerequisites = [[1,0]]))
        

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.