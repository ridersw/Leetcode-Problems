def getMinCost(cost, time):
    n = len(cost)
    dp = [[0, 0] for i in range(n+1)]
    dp[1][0] = cost[0]
    dp[1][1] = 0
    total_time = time[0]
    for i in range(2, n+1):
        dp[i][0] = min(dp[i-1][0] + cost[i-1], dp[i-1][1] + cost[i-1])
        dp[i][1] = dp[i-1][0] + time[i-1] + 1
        total_time += time[i-1]
    return min(dp[n][0], dp[n][1])

print(getMinCost(cost = [1,2,3,2], time = [1,2,3,2]))