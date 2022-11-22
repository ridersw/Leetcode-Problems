import collections

class Solution:
    def connectedGraph(self, n, edges):

        graph = collections.defaultdict(list)


        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        print(f'graph: {graph}')

        count = 0

        seen = set()

        for node in range(n):
            if node not in seen:
                self.dfs(node, graph, seen)
                count += 1

        
        print(f'seen: {seen} count: {count}')

    def dfs(self, node, graph, seen):
        if node not in seen:
            seen.add(node)
        else:
            return

        for swi in graph[node]:
            if swi not in seen:
                self.dfs(swi, graph, seen)

if __name__ == "__main__":
    obj = Solution()

    n = 5
    edges = [[0,1],[1,2],[3,4]]

    print(obj.connectedGraph(n, edges))

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