from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])

        dist = [[float("inf")] * n for _ in range(m)]

        start_cost = grid[0][0]
        dist[0][0] = start_cost

        dq = deque()
        dq.append((0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:
            r, c = dq.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = dist[r][c] + grid[nr][nc]

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost

                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return health - dist[m - 1][n - 1] >= 1