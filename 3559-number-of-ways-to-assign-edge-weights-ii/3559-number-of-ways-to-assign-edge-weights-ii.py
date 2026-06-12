from typing import List
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        n = len(edges) + 1
        LOG = 17

        while (1 << LOG) <= n:
            LOG += 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        up = [[0] * (n + 1) for _ in range(LOG)]

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            node = q.popleft()

            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    up[0][nei] = node
                    q.append(nei)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                up[k][v] = up[k - 1][up[k - 1][v]]

        def lca(a, b):

            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]

            for k in range(LOG):
                if diff & (1 << k):
                    a = up[k][a]

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]

            return up[0][a]

        max_depth = max(depth)
        pow2 = [1] * (max_depth + 1)

        for i in range(1, len(pow2)):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = []

        for u, v in queries:

            ancestor = lca(u, v)

            dist = depth[u] + depth[v] - 2 * depth[ancestor]

            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow(2, dist - 1, MOD))

        return ans