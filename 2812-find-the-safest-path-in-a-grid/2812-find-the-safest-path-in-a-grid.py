from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Multi-source BFS from all thieves
        distance = [[-1] * n for _ in range(n)]
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    distance[i][j] = 0
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < n
                    and 0 <= ny < n
                    and distance[nx][ny] == -1
                ):
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

        # Maximum bottleneck path using max heap
        maxDistancePath = [[-1] * n for _ in range(n)]

        heap = [(-distance[0][0], 0, 0)]
        maxDistancePath[0][0] = distance[0][0]

        while heap:
            negMinDist, x, y = heapq.heappop(heap)
            minDist = -negMinDist

            # Skip stale states
            if minDist < maxDistancePath[x][y]:
                continue

            if x == n - 1 and y == n - 1:
                return minDist

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    newMinDistance = min(minDist, distance[nx][ny])

                    if newMinDistance > maxDistancePath[nx][ny]:
                        maxDistancePath[nx][ny] = newMinDistance
                        heapq.heappush(
                            heap,
                            (-newMinDistance, nx, ny)
                        )

        return 0