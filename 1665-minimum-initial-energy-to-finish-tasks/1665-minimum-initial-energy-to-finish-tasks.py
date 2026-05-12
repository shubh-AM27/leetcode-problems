class Solution(object):
    def minimumEffort(self, tasks):

        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        temp = 0

        for i in range(len(tasks)):
            temp = max(temp, tasks[i][1])

        mini = temp

        for j in range(len(tasks)):

            if tasks[j][1] <= temp:

                temp = temp - tasks[j][0]

            else:

                mini += (tasks[j][1] - temp)

                temp = temp + (tasks[j][1] - temp)

                temp = temp - tasks[j][0]

        return mini
          