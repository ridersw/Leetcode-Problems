def taskScheduling(time, cost):
    tasks = len(cost)
    result = 0



    while tasks > 1:
        minimumCostTask = cost.index(min(cost))
        minimumCostTimeTask = time[minimumCostTask]

        print(f'minimumCostTask: {minimumCostTask} minimumCostTimeTask: {minimumCostTimeTask}')

        tasks -= 1
        result += minimumCostTimeTask

        time[minimumCostTask] = 1000001
        cost[minimumCostTask] = 1000001

        print(f'tasks: {tasks} result: {result}')
        while tasks > 0 and minimumCostTimeTask > 0:
            maximumCostTask = 0
            for swi in range(len(cost)):
                if maximumCostTask < cost[swi] and cost[swi] != 1000001:
                    pointer = swi
                    maximumCostTask = cost[swi]

            tasks -= 1
            minimumCostTimeTask -= 1
            time[pointer] = 1000001
            cost[pointer] = 1000001

    return result        
            

print(taskScheduling(time = [3,1,2,3], cost = [1,1,3,4]))
print(taskScheduling(time = [1,2,3,2], cost = [1,2,3,2]))