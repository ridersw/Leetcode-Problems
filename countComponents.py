
from collections import defaultdict
from email.policy import default


class Solution:
    def countComponents(self, n: int, edges):
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # print(f'Graph: {graph}')

        def bfs(node, seen):
            if node not in seen:
                seen.add(node)
            else:
                return 

            for swi in graph[node]:
                bfs(swi, seen)

        count = 0

        seen = set()
        for node in range(n):
            if node not in seen:
                bfs(node, seen)
                count += 1

        return count


if __name__ == "__main__":
    obj = Solution()

    print(obj.countComponents(n = 5, edges = [[0,1],[1,2],[3,4]])) # 2
    print(obj.countComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,4]])) # 1
    print(obj.countComponents(n = 4, edges = [[2,3],[1,2],[1,3]])) # 1
    print(obj.countComponents(n = 4, edges = [[0,1],[2,3],[1,2]])) # 1
    print(obj.countComponents(n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[3,5]])) #1

# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
 

# Constraints:

# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.