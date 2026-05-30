from sortedcontainers import SortedList

class Fenwick:

    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, val):

        while i < len(self.bit):
            self.bit[i] = max(self.bit[i], val)
            i += i & -i

    def query(self, i):

        ans = 0

        while i > 0:
            ans = max(ans, self.bit[i])
            i -= i & -i

        return ans


class Solution:

    def getResults(self, queries):

        LIMIT = 50000

        obstacles = SortedList([0, LIMIT])

        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        tree = Fenwick(LIMIT + 1)

        for i in range(len(obstacles) - 1):

            left = obstacles[i]
            right = obstacles[i + 1]

            tree.update(right, right - left)

        ans = []

        for q in reversed(queries):

            if q[0] == 1:

                x = q[1]

                idx = obstacles.index(x)

                prev = obstacles[idx - 1]
                nxt = obstacles[idx + 1]

                obstacles.remove(x)

                tree.update(nxt, nxt - prev)

            else:

                x, sz = q[1], q[2]

                idx = obstacles.bisect_right(x)

                prev = obstacles[idx - 1]

                ans.append(
                    tree.query(prev) >= sz
                    or x - prev >= sz
                )

        return ans[::-1]