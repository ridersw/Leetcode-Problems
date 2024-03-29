class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]
        
        # print(f'graph: {graph}')
        
        for u, v in edges:
            graph[v].add(u)
            graph[u].add(v)
            
        # print(f'graph: {graph}')
        
        leaves = [x for x in range(n) if len(graph[x]) <= 1]
        
        # print(f'leaves: {leaves}')
        
        prev_leaves = leaves
        
        while leaves:
            new_leaves = []
            
            for leaf in leaves:
                if not graph[leaf]:
                    return leaves
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            prev_leaves, leaves = leaves, new_leaves
            
        return prev_leaves
        
# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

# Example 1:
#d

# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
# Example 2:


# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]
# Example 3:

# Input: n = 1, edges = []
# Output: [0]
# Example 4:

# Input: n = 2, edges = [[0,1]]
# Output: [0,1]