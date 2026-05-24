class Solution:
    def maxJumps(self, arr, d):

        n = len(arr)

        dp = [-1] * n

        def dfs(i):

            if dp[i] != -1:
                return dp[i]

            best = 1

            for step in range(1, d + 1):

                left = i - step

                if left < 0 or arr[left] >= arr[i]:
                    break

                best = max(best, 1 + dfs(left))

            for step in range(1, d + 1):

                right = i + step

                if right >= n or arr[right] >= arr[i]:
                    break

                best = max(best, 1 + dfs(right))

            dp[i] = best

            return best

        answer = 0

        for i in range(n):

            answer = max(answer, dfs(i))

        return answer