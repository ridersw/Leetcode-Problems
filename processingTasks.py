class Solution:
    def processingTasks(self, tasks):
        timeActivate = []

        # tasksTimePeriod = []
        # tasksTimeRequired = []

        # for task in tasks:
        #     tasksTimeRequired.append(task[2])
        #     temp = []
        #     for swi in range(task[0],task[1]+1):
        #         temp.append(swi)
        #     tasksTimePeriod.append(temp)

        # print(f'tasksTimePeriod: {tasksTimePeriod}')
        # print(f'tasksTimeRequired: {tasksTimeRequired}')

        dict = {}

        for task in tasks:
            if task[2] in dict.keys():
                # key = task[2] + task[2]
                pass

                # dict[new_task] = dict[task[2]].pop()
            else:
                dict[task[2]] = []
                for swi in range(task[0], task[1]+1):
                    dict[task[2]].append(swi)


        print(f'dict: {dict}')
        print(f'dict[1]: {dict[2].keys()}')

if __name__ == "__main__":
    obj = Solution()

    tasks = [[1,3,2],[2,5,3],[5,6,2]]

    print(obj.processingTasks(tasks))