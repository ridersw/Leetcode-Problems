from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n, flights, source, destination, k):
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

        for src, des, pr in flights:
            adj_matrix[src][des] = pr

        distances = [float('inf') for _ in range(n)]
        curr_stops = [float('inf') for _ in range(n)]

        distances[source], curr_stops[source] = 0, 0

        #cost, stop, src
        minHeap = [(0, 0, source)]

        while minHeap:
            cost, stops, node = heapq.heappop(minHeap)

            if node == destination:
                return cost

            if stops == k+1:
                continue

            for neighbors in range(n):
                if adj_matrix[node][neighbors] > 0:
                    dU, dV, wUV = cost, distances[neighbors], adj_matrix[node][neighbors]

                    if dU + wUV < dV:
                        distances[neighbors] = dU + wUV
                        heapq.heappush(minHeap, (dU + wUV, stops+1, neighbors))

        return -1 if distances[k&1][destination] == float("inf") else distances[k&1][destination]


if __name__ == "__main__":
    obj = Solution()
    print(obj.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], source = 0, destination = 3, k = 1))

# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

# Example 1:


# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
# Example 2:


# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
# Example 3:


# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

# Constraints:

# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 104
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst