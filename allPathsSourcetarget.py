class Solution:
    def allPathsSourceTarget(self, graph):
        target = len(graph)-1
        result = []

        def backtrack(node, path):
            if node == target:
                result.append(list(path))
                return 

            for next_node in graph[node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        path = [0]
        backtrack(0, path)

        return result



if __name__ == "__main__":
    obj = Solution()

    print(obj.allPathsSourceTarget(graph = [[1,2],[3],[3],[]]))