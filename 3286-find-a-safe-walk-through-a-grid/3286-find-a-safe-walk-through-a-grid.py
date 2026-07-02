from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):

        m = len(grid)
        n = len(grid[0])

        health -= grid[0][0]

        if health <= 0:
            return False

        best = [[-1] * n for _ in range(m)]
        best[0][0] = health

        q = deque([(0, 0, health)])

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:

            x, y, hp = q.popleft()

            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in dirs:

                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n:

                    new_hp = hp - grid[nx][ny]

                    if new_hp <= 0:
                        continue

                    if new_hp > best[nx][ny]:

                        best[nx][ny] = new_hp
                        q.append((nx, ny, new_hp))

        return False